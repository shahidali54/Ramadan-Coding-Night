import streamlit as st  # Streamlit library for creating web-based applications
import time  # Time module for adding delays in execution

# Set up the page configuration with a title, icon, and layout
st.set_page_config(page_title="Next.Js Quiz App", page_icon="📋", layout="centered")

# Add custom CSS styling for better UI appearance
st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .question-card {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# Display the quiz title
st.markdown("<div class='title'>📋 Next.Js Quiz App</div>", unsafe_allow_html=True)

# Define the quiz questions with options and correct answers
questions = [
    {"question": "What is Next.js?", "options": ["A JavaScript library", "A React framework", "A CSS framework", "A backend language"], "answer": "A React framework"},
    {"question": "Which command is used to create a new Next.js app?", "options": ["npx create-next-app", "npm install next", "npx create-react-app", "npm init next-app"], "answer": "npx create-next-app"},
    {"question": "What file is used for routing in Next.js?", "options": ["index.js", "app.js", "page.tsx", "router.js"], "answer": "page.tsx"},
    {"question": "Which folder is used for automatic routing in Next.js?", "options": ["routes", "pages", "components", "public"], "answer": "pages"},
    {"question": "Which command is used to run a Next.js project in development mode?", "options": ["npm start", "next run", "npm run dev", "next build"], "answer": "npm run dev"},
    {"question": "Which function is used for server-side rendering (SSR) in Next.js?", "options": ["getStaticProps", "getServerSideProps", "useEffect", "fetch"], "answer": "getServerSideProps"},
    {"question": "Which function is used for static site generation (SSG) in Next.js?", "options": ["getServerSideProps", "getStaticProps", "useState", "useEffect"], "answer": "getStaticProps"},
    {"question": "Where do you place global styles in a Next.js project?", "options": ["index.css", "_app.js", "global.ts", "page.tsx"], "answer": "_app.js"},
    {"question": "Which component is used for navigation in Next.js?", "options": ["a", "Link", "Nav", "Router"], "answer": "Link"},
    {"question": "Which command is used to build a Next.js project for production?", "options": ["next run", "next build", "npm start", "npm build"], "answer": "next build"}
]

# Initialize session state variables if not already set
if "score" not in st.session_state:
    # User's quiz score
    st.session_state.score = 0  
if "question_index" not in st.session_state:
    # Tracks the current question number
    st.session_state.question_index = 0  

# Check if the quiz is complete
if st.session_state.question_index >= len(questions):
    st.markdown(f"### 🎉 Quiz Complete! Your Score: {st.session_state.score}/{len(questions)}")
    # Show balloons animation for completion
    st.balloons()
    # Stop execution
    st.stop()  

# Display quiz progress as a progress bar
progress = (st.session_state.question_index + 1) / len(questions)
st.progress(progress)

# Get the current question based on the session index
question = questions[st.session_state.question_index]
st.markdown(f"<div class='question-card'><h2>{question['question']}</h2></div>", unsafe_allow_html=True)

# Create radio buttons for answer selection
selected_option = st.radio("Select your answer:", question["options"], key="answer")

# Handle answer submission when the button is clicked
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        st.balloons()
        # Increment score if correct
        st.session_state.score += 1  
    else:
        st.error(f"❌ Incorrect! The correct answer is {question['answer']}")
    
    # Pause for 2 seconds before moving to the next question
    time.sleep(2)  
    # Move to the next question
    st.session_state.question_index += 1  
    # Refresh the page to load the next question
    st.rerun()  

# Display footer with the developer's credit
st.write("Made with ❤️ by [Shahid Ali](https://www.linkedin.com/in/shahid-ali-64676a2ba/)")
