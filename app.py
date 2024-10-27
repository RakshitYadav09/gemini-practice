from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("Google_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Gemini Pro", page_icon="🔮")

st.header("Gemini Pro")

input = st.text_input("Ask me anything", key="input")
submit= st.button("Ask")

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is:")
    st.write(response)