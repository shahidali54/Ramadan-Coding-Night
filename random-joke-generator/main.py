import streamlit as st
import requests

def get_random_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again later."
    except:
        return "Why did the programmer quit his job? \nBecause he didn't get array."

def main():
    # Set custom page config
    st.set_page_config(page_title="😂 Random Joke Generator", page_icon="😂", layout="centered")

    # Apply custom CSS styles for VVIP look + button hover + emoji rain + background gradient
    st.markdown("""
        <style>
            body, .stApp {
                background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
                animation: gradientBG 15s ease infinite;
            }

            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .title-text {
                font-size: 3rem;
                color: #FF4B4B;
                text-align: center;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .subtitle-text {
                font-size: 1.2rem;
                color: black;
                text-align: center;
                margin-bottom: 30px;
            }
            .footer {
                text-align: center;
                color: black;
                margin-top: 50px;
                font-size: 0.9rem;
            }
            .stButton>button {
                background: linear-gradient(90deg, #FF4B4B, #FF884B);
                color: blue;
                font-weight: bold;
                padding: 0.75rem 1.5rem;
                border-radius: 30px;
                transition: 0.4s;
                border: none;
            }
            .stButton>button:hover {
                background: black !important;
                color: white !important;
                transform: scale(1.1);
            }

            /* Emoji rain effect */
            .emoji-rain {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                overflow: hidden;
                z-index: 9999;
            }
            .emoji {
                position: absolute;
                font-size: 2rem;
                animation: fall linear infinite;
            }
            @keyframes fall {
                0% { transform: translateY(-100px); }
                100% { transform: translateY(110vh); }
            }
        </style>

        <div class="emoji-rain">
            <div class="emoji" style="left:10%; animation-duration: 5s;">😂</div>
            <div class="emoji" style="left:20%; animation-duration: 7s;">🤣</div>
            <div class="emoji" style="left:30%; animation-duration: 6s;">😆</div>
            <div class="emoji" style="left:50%; animation-duration: 8s;">😹</div>
            <div class="emoji" style="left:70%; animation-duration: 5.5s;">😁</div>
            <div class="emoji" style="left:80%; animation-duration: 7.5s;">😄</div>
        </div>
    """, unsafe_allow_html=True)

    # Title
    st.markdown("<div class='title-text'>😂 Joke Generator 😂</div>", unsafe_allow_html=True)

    # Subtitle
    st.markdown("<div class='subtitle-text'>Need a laugh? Click the button below to lighten up your mood!</div>", unsafe_allow_html=True)

    # Button with joke display
    if st.button("🎉 Generate Joke"):
        joke = get_random_joke()
        st.info(joke)

    # Divider with emoji
    st.markdown("---")
    st.markdown("<div class='subtitle-text'>✨ Keep Smiling ✨</div>", unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div class="footer">
            <p>Jokes powered by <a href="https://official-joke-api.appspot.com/" target="_blank">Official Joke API</a></p>
            <p>Built with ❤️ by <a href='https://www.linkedin.com/in/shahid-ali-64676a2ba/' target="_blank">Shahid Ali</a> using Streamlit</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
