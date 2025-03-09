import streamlit as st
import random
import time
import requests


# App title
st.title('🤑 Money Making Machine')

def generate_money():
    return random.randint(1, 1000)

st.subheader('Instan Cash Generator')
if st.button('Generate Money'):
    st.write('Counting your money...')
    time.sleep(1)
    amount = generate_money()
    st.success(f'You have earned ${amount}!')


def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustle")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return ("freelancing", "Freelance work")
        
    except:
        return("Somthing went wrong. Please try again later.")
    
st.subheader('Side Hustle Ideas')
if st.button('Genrete Hustle'):
    idea = fetch_side_hustle()
    st.success(idea)


def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quote")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return ("Money is the root of all evil!")
        
    except:
        return("Somthing went wrong!.")
    
st.subheader('Money Making Making Quotes')
if st.button('Get Inspired Quote'):
    quote = fetch_money_quote()
    st.success(quote)