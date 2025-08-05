import pdfplumber
from docx import Document

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_docx(file_path):
    """Extract text from a DOCX file."""
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
