import streamlit as st
from PIL import Image


st.title("Camera Example")
st.markdown('''
    Let's take a picture with the camera and conver the image to greyscale with PIL

    Learn More about PIL: https://pillow.readthedocs.io/en/stable/index.html
''')
pic_data = st.camera_input("Take a pic!")

if pic_data:
    img = Image.open(pic_data)
    grey_img = img.convert("L")
    st.image(grey_img)

