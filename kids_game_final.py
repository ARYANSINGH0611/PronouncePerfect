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
    "banana": "images/banana.jpg", 
    "dog": "images/dog.jpg", 
    "cat": "images/cat.jpg", 
    "car": "images/car.jpg", 
    "tree": "images/tree.jpg", 
    "sun": "images/sun.jpg", 
    "house": "images/house.jpg",  
    "bird": "images/bird.jpg", 
    "fish": "images/fish.jpg", 
    "elephant": "images/elephant.jpg", 
    "flower": "images/flower.jpg", 
    "star": "images/star.jpg", 
    "train": "images/train.jpg", 
    "book": "images/book.jpg", 
    "pen": "images/pen.jpg"
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
    st.title("🎮 Kids Learning Game")

    # Layout with two columns: one for the image and the other for the timer and feedback
    col1, col2 = st.columns([2, 3])  # Adjust columns ratio for optimal layout

    # Retain the same object if the child doesn't get it right
    if "current_object" not in st.session_state:
        st.session_state.current_object = random.choice(list(objects.items()))
        st.session_state.repeat_object = False  # To track whether the same object is being repeated
    object_name, image_file = st.session_state.current_object

    with col1:
        # Display the image with adjusted size and space
        st.image(image_file, caption="🖼️ What is this?", use_column_width=True)

    with col2:
        # Countdown Timer with Beep Sound
        st.subheader("⏳ **Get ready!**")
        timer_container = st.empty()
        timer_container.write("⏳ **Time starts now!**")

        for i in range(3, 0, -1):
            timer_container.write(f"⏰ **Time left: {i} seconds**")
            play_beep()  # Play beep sound for each second
            time.sleep(1)
        play_beep(frequency=700)  # Final sound to indicate "Speak now!"
        timer_container.write("⏰ **Time's up! Speak now!** 🎤")

        # Record audio using sounddevice
        audio_data, samplerate = record_audio(duration=5)
        temp_audio_file = save_audio(audio_data, samplerate)

        # Process the recorded audio with speech recognition
        recognizer = sr.Recognizer()
        result_container = st.empty()

        with sr.AudioFile(temp_audio_file) as source:
            try:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio).lower()
                result_container.write(f"🔊 **You said:** {text}")

                # Check if the response is correct
                if text == object_name:
                    st.balloons()
                    result_container.success("🎉 **Correct! Great Job!** 🎊")
                    play_audio("Well done! You got it right!")
                    time.sleep(2)  # Pause for feedback
                    st.session_state.current_object = random.choice(list(objects.items()))  # Move to the next object
                    st.session_state.repeat_object = False
                    st.experimental_rerun()
                else:
                    result_container.error("❌ **Oops! That's not quite right.**")
                    play_audio(f"The correct answer is {object_name}. Repeat after me.")
                    play_audio(object_name)
                    time.sleep(2)  # Ensure audio feedback completes before rerun
                    st.session_state.repeat_object = True  # Mark the object to be repeated
                    st.experimental_rerun()

            except sr.UnknownValueError:
                result_container.error("🤔 **Could not understand. Please try again!**")
                play_audio("I couldn't hear you. Let's try again!")
                time.sleep(2)  # Ensure audio feedback completes before rerun
            except sr.RequestError as e:
                result_container.error(f"⚠️ **Speech recognition error:** {e}")
                play_audio("There was an error with speech recognition. Please check your internet connection.")
                time.sleep(2)  # Ensure audio feedback completes before rerun

# Run the app
if __name__ == "__main__":
    main()
