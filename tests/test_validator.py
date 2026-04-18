from src.validator import validate_file

def test_valid_pdf_upload():
    assert validate_file("document.pdf", 2) == "Upload allowed"

def test_blocked_exe_file():
    assert validate_file("virus.exe", 1) == "Blocked file type"

def test_file_too_large():
    assert validate_file("image.jpg", 10) == "File too large"

def test_empty_filename():
    assert validate_file("", 1) == "Filename is empty"

def test_invalid_file_format():
    assert validate_file("myfile", 1) == "Invalid file format"