from pypdf import PdfReader

def extract_text(input_path: str) -> str:
    reader = PdfReader(input_path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)
