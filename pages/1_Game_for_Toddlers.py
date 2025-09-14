import streamlit as st
import time
import random
import speech_recognition as sr
from gtts import gTTS
import pygame
from io import BytesIO
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Initialize Pygame mixer for audio feedback
pygame.mixer.init()

# Object list and corresponding image paths
objects = {
    "apple": "images/apple.jpg",  
    "ball": "images/ball.jpg",
    "cup": "images/cup.jpg",
    "banana": "images/banana.jpeg", 
    "dog": "images/dog.jpeg", 
    "cat": "images/cat.jpeg", 
    "car": "images/car.jpeg", 
    "tree": "images/tree.jpeg", 
    "sun": "images/sun.jpeg", 
    "house": "images/house.jpeg",  
    "bird": "images/bird.jpeg", 
    "fish": "images/fish.jpeg", 
    "elephant": "images/elephant.jpeg", 
    "star": "images/star.jpeg", 
    "train": "images/train.jpeg", 
    "book": "images/book.jpeg", 
    "pen": "images/pen.jpeg"
}

# Function to play audio
def play_audio(text):
    tts = gTTS(text=text, lang='en')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    pygame.mixer.music.load(audio_bytes)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)  # Wait for the audio to finish playing

# Function to play a beep sound
def play_beep(duration=0.2, frequency=440):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Generate a sine wave
    sd.play(wave, samplerate=sample_rate)
    sd.wait()

# Function to record audio using sounddevice
def record_audio(duration=5, samplerate=44100):
    st.write("🎤 **Listening... Speak now!**")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    return audio_data, samplerate

# Function to save audio to a temporary file
def save_audio(audio_data, samplerate, filename="temp_audio.wav"):
    wav.write(filename, samplerate, audio_data)
    return filename

# Game logic
def main():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');
            .main > div {
                background: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
                font-family: 'Fredoka One', cursive;
            }
            .game-title {
                font-size: 3rem;
                color: #ff6347;
                text-align: center;
                padding: 20px;
            }
            .stImage > img {
                border-radius: 20px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.3);
            }
            .caption-text {
                font-size: 1.5rem;
                text-align: center;
                color: #555;
            }
            .timer-text {
                font-size: 2rem;
                color: #d9534f;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="game-title">Fun with Words!</h1>', unsafe_allow_html=True)

    # Layout with two columns
    col1, col2 = st.columns([2, 3])

    # Session state for current object
    if "current_object" not in st.session_state:
        st.session_state.current_object = random.choice(list(objects.items()))
        st.session_state.repeat_object = False
    object_name, image_file = st.session_state.current_object

    with col1:
        st.image(image_file, use_container_width=True)
        st.markdown('<p class="caption-text">What is this?</p>', unsafe_allow_html=True)

    with col2:
        st.subheader("Get Ready to Speak! 🎙️")
        timer_container = st.empty()
        
        for i in range(3, 0, -1):
            timer_container.markdown(f'<p class="timer-text">⏰ {i}</p>', unsafe_allow_html=True)
            play_beep()
            time.sleep(1)
        
        timer_container.markdown('<p class="timer-text">Speak Now!</p>', unsafe_allow_html=True)
        play_beep(frequency=700)

        # Record and process audio
        audio_data, samplerate = record_audio(duration=5)
        temp_audio_file = save_audio(audio_data, samplerate)
        recognizer = sr.Recognizer()
        result_container = st.empty()

        with sr.AudioFile(temp_audio_file) as source:
            try:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio).lower()
                result_container.info(f"You said: **{text}**")

                if text == object_name:
                    st.balloons()
                    result_container.success("🎉 Correct! You're a star! ⭐")
                    play_audio("Wow! That was amazing!")
                    time.sleep(2)
                    st.session_state.current_object = random.choice(list(objects.items()))
                    st.session_state.repeat_object = False
                    st.rerun()
                else:
                    result_container.error("Oops! Let's try that again. 💪")
                    play_audio(f"Not quite. This is a {object_name}. Say {object_name}.")
                    time.sleep(2)
                    st.session_state.repeat_object = True
                    st.rerun()

            except sr.UnknownValueError:
                result_container.warning("I didn't catch that. Let's try one more time! 🎤")
                play_audio("I couldn't hear you. Please speak a little louder.")
                time.sleep(2)
                st.rerun()
            except sr.RequestError:
                result_container.error("Oh no! We have a connection issue. 🔌")
                play_audio("There seems to be a problem with the internet connection.")
                time.sleep(2)
                st.rerun()

# Run the app
if __name__ == "__main__":
    main()
