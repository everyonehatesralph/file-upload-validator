import streamlit as st
from src.validator import validate_file

# Page setup
st.set_page_config(page_title="File Upload Validator", page_icon="📁")

# Title
st.title("File Upload Validator")

# Description
st.write("Enter a file name and size to validate it.")

# Inputs
filename = st.text_input("File Name", placeholder="example.pdf")
file_size = st.number_input("File Size (MB)", min_value=0.0, step=0.1)

# Button
if st.button("Validate File"):
    result = validate_file(filename, file_size)
    st.success(result)