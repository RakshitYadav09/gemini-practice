from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("Google_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Pro Vision", page_icon="🔮")

st.header("Gemini Pro Vision")

input = st.text_input("Ask me anything", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="image")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
submit = st.button("Ask")
if submit:
    
    response = get_gemini_response(input, image) 
    st.subheader("The response is:") 
    st.write(response)
        