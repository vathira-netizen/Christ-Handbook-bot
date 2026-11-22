import fitz
from langchain_core.documents import Document

def load_pdf(pdf_path):
    docs = []

    pdf = fitz.open(pdf_path)

    for page_num in range(len(pdf)):
        page = pdf[page_num]
        text = page.get_text()

        docs.append(
            Document(
                page_content=text,
                metadata={
                    "page": page_num + 1
                }
            )
        )

    return docs