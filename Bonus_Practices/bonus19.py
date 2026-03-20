import streamlit as st
from PIL import Image
from PIL.ImageOps import grayscale

st.subheader("Color to Grayscale converter")
with st.expander("Start camera"):
    #start the camera
    camera_image = st.camera_input("Camera")
image = st.file_uploader("Upload Image")

if camera_image:
    #create a pillow image instance
    img = Image.open(camera_image)
    #convert to gray scale
    gray_img = img.convert("L")
    #render the gray scale image on the web page
    st.image(gray_img)

if image:

    uploaded_image = Image.open(image)
    gray_pic = uploaded_image.convert("L")
    st.image(gray_pic)
