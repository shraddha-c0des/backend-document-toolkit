# 🚀 Backend AI Tool Layer - Document Toolkit

A production-ready, modular, and scalable backend micro-service built with **FastAPI**, **PyMuPDF**, and **PaddleOCR** designed to handle complex document processing pipelines.

---

## 🛠️ Architecture & Structure
This repository is split into two decoupled layers for high scalability:
1. **API Routing Layer (`/app/api/`)**: Presentation & endpoint validation handling incoming HTTP requests.
2. **Business Services Layer (`/app/services/`)**: Core processing engines running PDF manipulation and OCR workloads.

---

## 📦 Features Included
* **PDF Merge**: Combine multiple PDF files seamlessly.
* **OCR Extraction**: Extract structured text from scanned image-based documents using PaddleOCR.

---

## 🚀 Quick Start
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/backend-document-toolkit.git](https://github.com/YOUR_USERNAME/backend-document-toolkit.git)
   cd backend-document-toolkit
