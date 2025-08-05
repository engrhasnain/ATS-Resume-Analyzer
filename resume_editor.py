from docx import Document
from io import BytesIO

def update_resume_file(corrected_text):
    """Generate a corrected Word file in memory and return it as BytesIO."""
    doc = Document()
    for line in corrected_text.split("\n"):
        if line.strip():
            doc.add_paragraph(line)

    file_stream = BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)
    return file_stream
