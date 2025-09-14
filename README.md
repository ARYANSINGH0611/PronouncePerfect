# Speech Disorder Detection And Correction System 

## Overview
This pipeline is designed to help children improve their pronunciation and vocabulary through interactive learning activities. The game presents two modes of play:
1. **Object Identification Mode**: Displays an image of a regular object. The child has to speak the name of the object when prompted.
2. **Sentence Reading Mode**: Displays a short story, sentence by sentence, and the child reads aloud. Feedback is provided on mispronunciations or stammering.

The game dynamically adjusts the experience to ensure children learn effectively, with real-time feedback and guidance.

---

## Features
### Object Identification Mode
- Displays an image of a common object (e.g., apple, car, dog).
- A timer counts down, after which the microphone is enabled.
- The child speaks the name of the object aloud.
- **Correct Response**: Moves to the next image.
- **Incorrect Response**: The game repeats the correct name and prompts the child to try again.

### Sentence Reading Mode
- Displays a short, moral-based story, sentence by sentence.
- The child reads each sentence aloud.
- **Feedback Mechanism**:
  - Detects stammering or mispronunciation.
  - Repeats the sentence as audio output.
  - The child must re-read the current sentence until pronounced correctly.
- Includes a **Hint Button**: Pronounces the current sentence word by word to assist the child.

---

## Workflow
1. **Image-Based Interaction**:
   - Timer counts down.
   - Speech is captured through a microphone.
   - Speech-to-text conversion occurs.
   - Text is matched against the object name for validation.
2. **Story-Based Interaction**:
   - Sentence from the story is displayed.
   - Child’s speech is analyzed using speech-to-text.
   - Validation for correct pronunciation.
   - Cursor updates to the next sentence upon successful pronunciation.
   - Feedback provided for errors, prompting the child to repeat.
3. **Feedback Loop**:
   - Visual and audio feedback ensures engagement.
   - Repeat mechanisms reinforce learning.

---

## Technologies Used
- **Streamlit**: For developing the user interface.
- **Speech-to-Text API**: Converts the child’s speech into text for analysis.
- **Python Libraries**:
  - `speech_recognition`: For capturing and processing audio.
  - `Pillow`: For displaying images.
  - `pygame`: For playing audio feedback.
- **Natural Language Processing (NLP)**:
  - Used for analyzing speech and providing feedback.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ARYANSINGH0611/PronouncePerfect.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage
1. Launch the game.
2. Select the desired mode: **Object Identification** or **Sentence Reading**.
3. Follow the on-screen instructions to complete the activity.
4. Use the feedback to improve pronunciation and vocabulary.

---

## Future Improvements
- Expand the object image database with more diverse objects.
- Add difficulty levels for story complexity and vocabulary.
- Incorporate multilingual support for non-English learners.
- Include gamified rewards to enhance engagement.

---

## Contribution
Contributions are welcome! Please open an issue or submit a pull request for any feature suggestions or bug fixes.



