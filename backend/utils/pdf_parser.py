# backend/utils/pdf_parser.py

import PyPDF2

def extract_text_from_pdf(file_path: str):
    """
    Reads PDF and returns extracted text as string.
    """
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        return f"PDF_PARSE_ERROR: {e}"
