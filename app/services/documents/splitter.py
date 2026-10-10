from pypdf import PdfReader, PdfWriter
from pathlib import Path
import zipfile

def split_pdf(input_path: str, output_dir: str) -> str:
    reader = PdfReader(input_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    zip_path = output_path / "split_pages.zip"

    with zipfile.ZipFile(zip_path, "w") as z:
        for i, page in enumerate(reader.pages, start=1):
            writer = PdfWriter()
            writer.add_page(page)
            page_path = output_path / f"page_{i}.pdf"
            with open(page_path, "wb") as f:
                writer.write(f)
            z.write(page_path, arcname=page_path.name)
            page_path.unlink()

    return str(zip_path)
