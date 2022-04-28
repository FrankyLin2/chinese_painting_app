import streamlit as st
from PIL import Image
import cv2
import numpy as np
from test import main

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Oringinal Picture')
    image.save("input.jpg")
    main("input.jpg")
    result = Image.open("resizedresult.png")
    st.image(result, caption='Converted Picture')
picture = st.camera_input("Take a picture")
if picture:
    image = Image.open(picture)
    st.image(image, caption='Oringinal Picture')
    image.save("input.jpg")
    main("input.jpg")
    result = Image.open("resizedresult.png")
    st.image(result, caption='Converted Picture')
with open("resizedresult.png", "rb") as file:
     btn = st.download_button(
             label="Download image",
             data=file,
             file_name="result.png",
             mime="image/png"
           )