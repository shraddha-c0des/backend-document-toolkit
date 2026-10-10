from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
import shutil
from app.services.documents import merger

router = APIRouter()
TEMP_DIR = "/tmp/documents"
os.makedirs(TEMP_DIR, exist_ok=True)

@router.post("/merge", summary="Merge multiple PDFs into one")
async def merge_pdfs_endpoint(files: list[UploadFile] = File(...)):
    saved_paths = []
    try:
        for file in files:
            path = os.path.join(TEMP_DIR, file.filename)
            with open(path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            saved_paths.append(path)
        
        output_path = os.path.join(TEMP_DIR, "merged_output.pdf")
        merger.merge_pdfs(saved_paths, output_path)
        return FileResponse(output_path, media_type="application/pdf", filename="merged.pdf")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from app.services.documents import splitter

@router.post("/split")
async def split_pdf_endpoint(file: UploadFile = File(...)):
    input_path = os.path.join(TEMP_DIR, file.filename)

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_dir = os.path.join(TEMP_DIR, "split_output")
    zip_path = splitter.split_pdf(input_path, output_dir)

    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename="split_pages.zip"
    )

from app.services.documents import text_extractor

@router.post("/extract-text")
async def extract_pdf_text(file: UploadFile = File(...)):
    input_path = os.path.join(TEMP_DIR, file.filename)

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = text_extractor.extract_text(input_path)
    return {"text": text}

from app.services.documents import pdf_info

@router.post("/pdf-info")
async def get_pdf_info_endpoint(file: UploadFile = File(...)):
    input_path = os.path.join(TEMP_DIR, file.filename)

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return pdf_info.get_pdf_info(input_path)