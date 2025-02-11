import streamlit as st
from google import genai
st.set_page_config(
    page_title = 'mehmeh',
    page_icon = '✈️',
    layout = 'wide'
)

client = genai.Client(api_key="")

textbox = st.text_input("Type what you want to ask Gemini here")

if st.button("Submit to ask gemini"):
    response2 = client.models.generate_content(
    model='gemini-2.0-flash', 
    contents=textbox
)
    st.write(response2.text)