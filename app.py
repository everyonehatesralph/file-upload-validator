import streamlit as st
from src.validator import validate_file
import re
import os

# =========================
# 🔐 AUTHENTICATION
# =========================
APP_PASSWORD = os.getenv("APP_PASSWORD")

st.set_page_config(page_title="File Upload Validator", page_icon="📁")

st.title("File Upload Validator")

# If password not set (safety check)
if not APP_PASSWORD:
    st.error("App password not configured. Contact developer.")
    st.stop()

# Login input
password = st.text_input("Enter password to access app", type="password")

if password != APP_PASSWORD:
    st.warning("Unauthorized access")
    st.stop()

# =========================
# 📄 APP CONTENT (Protected)
# =========================

st.write("Enter a file name and size to validate it.")

filename = st.text_input("File Name", placeholder="example.pdf")
file_size = st.number_input("File Size (MB)", min_value=0.0, max_value=100.0, step=0.1)

# =========================
# ✅ INPUT VALIDATION
# =========================

def is_valid_filename(name):
    return bool(re.match(r'^[\w\-. ]+$', name))

# =========================
# 🚀 MAIN ACTION
# =========================

if st.button("Validate File"):
    if not filename:
        st.error("Filename is required")
    elif not is_valid_filename(filename):
        st.error("Invalid filename format")
    elif file_size <= 0:
        st.error("File size must be greater than 0")
    else:
        result = validate_file(filename, file_size)
        st.success(result)