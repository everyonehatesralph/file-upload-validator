from turtle import st


ALLOWED_EXTENSIONS = [".pdf", ".docx", ".png", ".jpg"]
BLOCKED_EXTENSIONS = [".exe", ".bat", ".js", ".sh"]
MAX_SIZE_MB = 5
WARNING_THRESHOLD_MB = 4


def is_filename_empty(filename):
    return not filename or filename.strip() == ""


def get_file_extension(filename):
    if "." not in filename:
        return None
    return filename[filename.rfind("."):].lower()


def is_blocked_extension(extension):
    return extension in BLOCKED_EXTENSIONS


def is_allowed_extension(extension):
    return extension in ALLOWED_EXTENSIONS


def is_file_empty(file_size_mb):
    return file_size_mb <= 0


def is_file_too_large(file_size_mb):
    return file_size_mb > MAX_SIZE_MB


def is_near_size_limit(file_size_mb):
    return WARNING_THRESHOLD_MB <= file_size_mb <= MAX_SIZE_MB

def is_valid_filename(name):
    # only allow letters, numbers, dot, dash, underscore
    return bool(re.match(r'^[\w\-. ]+$', name))



def validate_file(filename, file_size_mb):
    if is_filename_empty(filename):
        return "Filename is empty"

    extension = get_file_extension(filename)
    if extension is None:
        return "Invalid file format"

    if is_blocked_extension(extension):
        return "Blocked file type"

    if not is_allowed_extension(extension):
        return "File type not allowed"

    if is_file_empty(file_size_mb):
        return "File is empty"

    if is_file_too_large(file_size_mb):
        return "File too large"

    if is_near_size_limit(file_size_mb):
        return "Warning: File is near the size limit"

    return "Upload allowed"