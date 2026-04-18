def validate_file(filename, file_size_mb):
    allowed_extensions = [".pdf", ".docx", ".png", ".jpg"]
    blocked_extensions = [".exe", ".bat", ".js", ".sh"]
    max_size_mb = 5

    if not filename or filename.strip() == "":
        return "Filename is empty"

    filename = filename.lower()

    if "." not in filename:
        return "Invalid file format"

    extension = filename[filename.rfind("."):]

    if extension in blocked_extensions:
        return "Blocked file type"

    if extension not in allowed_extensions:
        return "File type not allowed"

    if file_size_mb <= 0:
        return "File is empty"

    if file_size_mb > max_size_mb:
        return "File too large"

    return "Upload allowed"