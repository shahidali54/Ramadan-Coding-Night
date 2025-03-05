import streamlit as st         # Importing the Streamlit library
import random                  # Importing the random library
import string                  # Importing the string library

# Function to Generate a Password based on the user's preferences
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Include All letters (a-z, A-Z)

    if use_digits:
        characters += string.digits  # Add numbers (0-9)

    if use_special:
        characters += string.punctuation  # Add special characters (!, @, #, $, %, ^, &, *)

    # Generate a random password of the specified length using the characters defined above
    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}` ")

st.write("---------------------------------")

st.write("Build with ❤️ by [Shahid Ali]")