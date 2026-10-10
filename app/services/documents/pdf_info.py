from pypdf import PdfReader

def get_pdf_info(input_path: str) -> dict:
    reader = PdfReader(input_path)
    return {
        "page_count": len(reader.pages),
        "metadata": {str(k): str(v) for k, v in (reader.metadata or {}).items()}
    }
