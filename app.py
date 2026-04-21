import streamlit as st
from src.validator import validate_file
import re
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Authentication
APP_PASSWORD = os.getenv("APP_PASSWORD")

st.set_page_config(page_title="File Upload Validator", page_icon="📁")
st.title("File Upload Validator")

# Stop app if password is not configured
if not APP_PASSWORD:
    st.error("App password not configured. Contact developer.")
    st.stop()

# Login
password = st.text_input("Enter password to access app", type="password")

if password != APP_PASSWORD:
    st.warning("Unauthorized access")
    st.stop()

# App content
st.write("Enter a file name and size to validate it.")

filename = st.text_input("File Name", placeholder="example.pdf")
file_size = st.number_input("File Size (MB)", min_value=0.0, max_value=100.0, step=0.1)

# Input validation helper
def is_valid_filename(name):
    return bool(re.match(r'^[\w\-. ]+$', name))

# Main action
if st.button("Validate File"):
    logging.info(f"Input received: filename={filename}, size={file_size}")

    if not filename:
        logging.warning("Validation failed: empty filename")
        st.error("Filename is required")

    elif not is_valid_filename(filename):
        logging.warning(f"Validation failed: invalid filename format ({filename})")
        st.error("Invalid filename format")

    elif file_size <= 0:
        logging.warning(f"Validation failed: invalid file size ({file_size})")
        st.error("File size must be greater than 0")

    else:
        result = validate_file(filename, file_size)
        logging.info(f"Validation result: {result}")
        st.success(result)