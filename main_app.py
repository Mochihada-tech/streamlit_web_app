import streamlit as st
from PIL import Image

st.title('sampleApps')
st.caption('This is test apps')


image = Image.open('./data/dog.jpg')
st.image(image, width=200)

image2 = Image.open('./data/git-new-repository.png')
st.image(image2, width=300)