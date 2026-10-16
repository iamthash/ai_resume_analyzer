from pypdf import PdfReader
from docx import Document
from pathlib import Path
from io import BytesIO
def extract_text(uploaded_file):
    extension = Path(uploaded_file.name).suffix.lower()
    file_bytes = BytesIO(uploaded_file.getvalue())
    if extension == ".pdf":
        reader = PdfReader(file_bytes)
        text = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )
    elif extension == ".docx":
        document = Document(file_bytes)
        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )
    else:
        raise ValueError("Only PDF and DOCX files are supported.")
    return text.strip()