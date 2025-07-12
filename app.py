import streamlit as st
from PIL import Image
st.title("Hello Page")
st.write("Upload a Image")
upload_file=st.file_uploader("Choose your file.......",type=["jpeg","jpg","png"])
if upload_file is not None:
  st.success("Successfully Uploaded")
  image=Image.open(upload_file)
  st.image(image,caption="Uploaded Image")
  
