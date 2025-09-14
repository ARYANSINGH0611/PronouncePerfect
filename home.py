import streamlit as st

# Set page config
st.set_page_config(page_title="PronouncePerfect", page_icon="�", layout="wide")

# Colorful and fun UI using custom CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans:wght@700&display=swap');

        .main > div {
            background-color: #87CEEB; /* Sky Blue */
            background-image: 
                url('https://www.transparenttextures.com/patterns/stars.png'); /* Star pattern */
            font-family: 'Balsamiq Sans', cursive;
        }

        .main-title {
            font-size: 6rem;
            color: #FFD700; /* Gold */
            text-align: center;
            animation: pulse 2s infinite;
            text-shadow: 5px 5px 0px #FF6347; /* Tomato */
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        .intro-text {
            font-size: 2rem;
            color: #32CD32; /* Lime Green */
            text-align: center;
            margin: 30px;
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 25px;
            border: 5px dashed #FF69B4; /* Hot Pink */
        }

        .instructions {
            background-color: #fff;
            border-radius: 20px;
            padding: 25px;
            margin: 30px auto;
            max-width: 800px;
            border: 5px solid #32CD32; /* Lime Green */
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        }

        .instructions h2 {
            color: #FF6347; /* Tomato */
            text-align: center;
            font-size: 2.5rem;
        }

        .instructions p {
            color: #000;
            font-size: 1.2rem;
            line-height: 1.6;
        }

        .stButton>button {
            background-color: #FFD700; /* Gold */
            color: #FF6347; /* Tomato */
            border-radius: 50px;
            padding: 20px 40px;
            font-size: 1.8rem;
            font-family: 'Balsamiq Sans', cursive;
            border: 5px solid #FF6347;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #FF6347;
            color: #FFD700;
            transform: rotate(5deg) scale(1.1);
            box-shadow: 0 12px 24px rgba(0,0,0,0.3);
        }

        .footer {
            text-align: center;
            padding: 20px;
            font-size: 1.5rem;
            color: #fff;
            background: linear-gradient(45deg, #FF69B4, #FFD700, #32CD32, #87CEEB);
            border-radius: 20px;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-title">PronouncePerfect</h1>', unsafe_allow_html=True)

# Introduction
st.markdown('<p class="intro-text">Let\'s go on a magical journey of words! 🦄✨</p>', unsafe_allow_html=True)

# Instructions Section
st.markdown("""
    <div class="instructions">
        <h2>How to Play! 🎮</h2>
        <p>
            <strong>🎈 Game for Toddlers:</strong>
            <br>
            1. Look at the picture on the screen.
            <br>
            2. When the timer ends, say the name of the object out loud!
            <br>
            3. Get it right and celebrate with balloons! 🥳
        </p>
        <br>
        <p>
            <strong>📚 Game for Younger Kids:</strong>
            <br>
            1. Read the sentence shown on the screen.
            <br>
            2. Click the "Record Audio" button and read the sentence.
            <br>
            3. If you get stuck, click the "Hint" button to hear the sentence.
            <br>
            4. Read the whole story to win! 🏆
        </p>
    </div>
""", unsafe_allow_html=True)

# Sidebar instructions
st.sidebar.header("🚀 Ready for an Adventure?")
st.sidebar.info("Pick a game from the list above and let the fun begin!")

# Footer
st.markdown('<div class="footer">Happy Learning, Little Sprouts! 🌱</div>', unsafe_allow_html=True)

