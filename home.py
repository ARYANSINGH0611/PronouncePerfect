import streamlit as st
import subprocess

# Set the title of the web app
st.title("🎮 Kids Learning Games")

# Add background color and fun font
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .big-font {
            font-size: 36px !important;
            color: #ff6347;
            font-weight: bold;
            text-align: center;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }
        .button-style {
            background-color: #ff7f50;
            color: white;
            border-radius: 12px;
            padding: 15px 30px;
            font-size: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s, background-color 0.3s ease;
        }
        .button-style:hover {
            transform: scale(1.1);
            background-color: #ff6347;
        }
        .container-style {
            text-align: center;
            padding: 20px;
            background-color: #ffebcd;
            border-radius: 15px;
        }
        .footer-text {
            text-align: center;
            font-size: 18px;
            color: #333;
            padding: 10px;
            background-color: #ffebcd;
            border-radius: 10px;
        }
        .img-container {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
        }
    </style>
""", unsafe_allow_html=True)

# Display the introduction
st.write("""
Welcome to **Kids Learning Games**! Choose a game that suits your child's age group and start learning in a fun and interactive way. 🌟
""")

# Display the custom heading
st.markdown('<p class="big-font">Select a Game to Start</p>', unsafe_allow_html=True)

# Display the image for added visual appeal
st.image("image.png", caption="Learning made fun! 🤩", use_column_width=True)

# Create a container for a more engaging layout
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        # Add a visually appealing button with an icon and hover effect
        if st.button("🧸 Game for Toddlers", key="small_kids", help="Click to start the small kids game", use_container_width=True, on_click=lambda: st.success("Starting the Game for Small Kids... 🎉")):
            subprocess.run(["streamlit", "run", "kids_game_final.py"])

    with col2:
        # Add a visually appealing button with an icon and hover effect
        if st.button("📚 Game for Younger Kids", key="older_kids", help="Click to start the older kids game", use_container_width=True, on_click=lambda: st.success("Starting the Game for Older Kids... 📖")):
            subprocess.run(["streamlit", "run", "older_games_final.py"])

# Add footer with fun text
st.markdown("""<div class="footer-text">Learning made fun for kids of all ages! 🎉</div>""", unsafe_allow_html=True)
