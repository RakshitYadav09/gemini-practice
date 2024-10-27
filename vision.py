from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("Google_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

 
    