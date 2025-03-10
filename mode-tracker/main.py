import streamlit as st  # for creating web interface
import pandas as pd     # for data manipulation
import datetime         # for handling dates
import csv              # for readin and writing CSV file
import os               # for file operations


# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# Function to read mood data from the CSV file
def load_mood_data():

     # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # If no file, create empty DataFrame with columns
        return pd.DataFrame(columns=["Date", "Mood" ])
      # Read and return existing mood data
    return pd.read_csv(MOOD_FILE)

# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
    # Open file in append mode
    with open(MOOD_FILE, "a", encoding="utf-8") as file:

        # Create CSV writer
        writer = csv.writer(file)
        
        # Add new mood entry
        writer.writerow([date, mood])

# Streamlit app title
st.title("🤔 Mood Tracker")

# Get today's date
today = datetime.date.today()

# Create subheader for mood input
st.subheader("How Are You Feeling Today?")

# Create dropdown for mood selection
mood = st.selectbox(
    "Select your mood:",
    ["😄 Very Happy", "🙂 Happy", "😐 Neutral", " ☹️ Sad", "😢 Very Sad", "😠 Angry"]
)

# Create button to save mood
if st.button("Log Mood"):

    # st.balloons()

    # Save mood when button is clicked
    save_mood_data(today, mood)

    # Show success message
    st.success("Mood logged successfully!")

# Load existing mood data
data = load_mood_data()

# If there is data to display
if not data.empty:

    # Create section for Visualization
    st.subheader("Mood Trends Over Time")

    # Convert date stings to datetime Objects
    data["Date"] = pd.to_datetime(data["Date"])

    # Count frequency of each mood
    mood_counts = data.groupby("Mood").count()["Date"]

    # Create a bar chart to display mood trends over time
    st.bar_chart(mood_counts)

# Build with love by Shahid Ali
st.write("Build with ❤️ by [Shahid Ali](https://www.linkedin.com/in/shahid-ali-64676a2ba/)")