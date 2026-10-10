import streamlit as st
import requests

API = "http://127.0.0.1:8000/api/v1/documents"

st.title("📄 PDF Document Toolkit")
st.write("Merge, split, extract text, and inspect PDF files.")

feature = st.selectbox(
    "Choose a function",
    ["Merge PDFs", "Split PDF", "Extract Text", "PDF Information"]
)

multiple = feature == "Merge PDFs"
files = st.file_uploader(
    "Upload PDF file(s)",
    type=["pdf"],
    accept_multiple_files=multiple
)

if st.button("Process PDF"):
    if files:
        try:
            with st.spinner("Processing..."):
                if feature == "Merge PDFs":
                    data = [
                        ("files", (f.name, f.getvalue(), "application/pdf"))
                        for f in files
                    ]
                    response = requests.post(f"{API}/merge", files=data)

                else:
                    file = files
                    data = {
                        "file": (file.name, file.getvalue(), "application/pdf")
                    }
                    endpoint = {
                        "Split PDF": "split",
                        "Extract Text": "extract-text",
                        "PDF Information": "pdf-info"
                    }[feature]
                    response = requests.post(f"{API}/{endpoint}", files=data)

            if response.status_code == 200:
                if feature == "Merge PDFs":
                    st.download_button(
                        "Download Merged PDF", response.content,
                        "merged.pdf", "application/pdf"
                    )
                elif feature == "Split PDF":
                    st.download_button(
                        "Download Split Pages ZIP", response.content,
                        "split_pages.zip", "application/zip"
                    )
                elif feature == "Extract Text":
                    st.text_area("Extracted Text", response.json()["text"], height=300)
                    st.download_button(
                        "Download Text", response.json()["text"],
                        "extracted.txt", "text/plain"
                    )
                else:
                    st.success("PDF information retrieved!")
                    st.json(response.json())
            else:
                st.error(f"Error: {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("Start your FastAPI backend first!")
    else:
        st.warning("Please upload a PDF file.")