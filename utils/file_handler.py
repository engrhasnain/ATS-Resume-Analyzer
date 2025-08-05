import os

def save_uploaded_file(uploaded_file):
    """Save uploaded file temporarily and return file path."""
    file_path = os.path.join("temp_" + uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path
