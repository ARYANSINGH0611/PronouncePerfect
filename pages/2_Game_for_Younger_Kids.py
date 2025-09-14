import pyttsx3
import sounddevice as sd
import numpy as np
import speech_recognition as sr
import streamlit as st
import wavio
import time
import string
import tempfile
from pydub import AudioSegment
from pydub.playback import play

# Set page config as the first Streamlit command
st.set_page_config(page_title="Reading Game", page_icon="📖", layout="wide")

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 120)  # Slow down speech for clarity

# Function to spell out the sentence as a hint
def spell_sentence(current_sentence):
    try:
        temp_wav_file = tempfile.mktemp(suffix=".wav")
        engine.save_to_file(f"Here's your hint. {current_sentence}", temp_wav_file)
        engine.runAndWait()

        # Play audio using pydub
        audio = AudioSegment.from_wav(temp_wav_file)
        play(audio)

        st.success("Hint provided successfully! 🟢")
    except Exception as e:
        st.error(f"Error providing hint: {str(e)}")

# Function to capture real-time audio using sounddevice
def record_audio(duration=5, samplerate=16000):
    try:
        st.info("Recording... Speak now! 🎤")
        audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        st.success("Recording stopped! Processing your audio... 🔄")
        return audio_data.flatten()  # Flatten to 1D array
    except Exception as e:
        st.error(f"Error during recording: {str(e)}")

# Save recorded audio to a WAV file
def save_audio_to_wav(audio_data, samplerate=16000, filename="temp_audio.wav"):
    wavio.write(filename, audio_data, samplerate, sampwidth=2)  # 2 bytes per sample
    return filename

# Function to display the sentence for reading
def show_sentence(sentence):
    st.markdown(f"### {sentence}", unsafe_allow_html=True)

# Function to display the full story
def show_full_story():
    st.markdown("## Full Story: ")
    show_sentence("It was a sunny day. Anna went to the park with her dog. She played with a ball while the dog ran around. They sat under a tree and ate sandwiches. Anna was happy to spend a peaceful day outside.")

# Preprocessing function to standardize text for comparison
def preprocess_text(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation))

# Main function for the Streamlit app
def main():
    st.title("📖 A Day in the Park")

    # Story sentences
    story = [
        "It was a sunny day.",  
        "Anna went to the park with her dog.",  
        "She played with a ball while the dog ran around.",  
        "They sat under a tree and ate sandwiches.",  
        "Anna was happy to spend a peaceful day outside."
    ]

    # Session state to keep track of current sentence
    if "current_sentence_index" not in st.session_state:
        st.session_state.current_sentence_index = 0

    # Buttons to toggle between sentence-by-sentence mode and full story
    col1, col2 = st.columns(2)
    with col1:
        if st.button("View Full Story 📖"):
            show_full_story()
    with col2:
        if st.button("Next Sentence 🎮"):
            current_sentence_index = st.session_state.current_sentence_index
            current_sentence = story[current_sentence_index]
            show_sentence(current_sentence)

    # Display the current sentence in sentence-by-sentence mode
    current_sentence_index = st.session_state.current_sentence_index
    current_sentence = story[current_sentence_index]
    show_sentence(current_sentence)

    # "Hint" button to spell out the sentence
    if st.button("Hint 💡"):
        spell_sentence(current_sentence)

    # "Record Audio" button for real-time input
    if st.button("Record Audio 🎤"):
        audio_data = record_audio(duration=8)
        wav_filename = save_audio_to_wav(audio_data)

        # Process audio with speech recognition
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_filename) as source:
            audio = recognizer.record(source)

        try:
            user_input = recognizer.recognize_google(audio)
            st.write(f"🔊 You said: {user_input}")

            # Preprocess both the user input and the current sentence
            processed_input = preprocess_text(user_input)
            processed_sentence = preprocess_text(current_sentence)

            # Compare the processed texts
            if processed_input == processed_sentence:
                st.success("🎉 Perfect pronunciation! 🗣")
                # Move to the next sentence
                st.session_state.current_sentence_index += 1
                if st.session_state.current_sentence_index >= len(story):
                    st.balloons()
                    st.success("🎉 Congratulations! You finished the story! 🎉")
                    st.session_state.current_sentence_index = 0
            else:
                st.error("❌ There were some errors in your pronunciation. Try again.")
        except sr.UnknownValueError:
            st.error("😞 Could not understand your speech. Please try again.")

    # Restart button
    if st.button("Restart Story 🔄"):
        st.session_state.current_sentence_index = 0

if __name__ == "__main__":
    main()
