import os
import streamlit as st
from google import genai

st.set_page_config(
    page_title="SUTD AI Ig page",
    page_icon=":robot_face:",  # Favicon emoji
    layout="wide",  # Page layout option
)

st.title("Welcome to the SUTD AI Interest Group Website")

client = genai.Client(api_key="")

response = client.models.generate_content(
    model='gemini-2.0-flash', 
    contents='Help me make an introduction about what a university AI club does in 1 paragraph'
)


st.write(response.text)


