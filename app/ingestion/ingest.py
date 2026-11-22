"""
Ingestion pipeline: PDF -> page documents -> chunks -> embeddings -> Chroma.

Run from the project root:
    python -m app.ingestion.ingest
"""
import os

from dotenv import load_dotenv

from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_documents
from app.ingestion.embedder import create_vector_store

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH", os.path.join("data", "handbook.pdf"))


def main():

    if not os.path.exists(PDF_PATH):
        raise FileNotFoundError(
            f"Handbook PDF not found at '{PDF_PATH}'. "
            "Place the PDF there or set PDF_PATH in your .env file."
        )

    docs = load_pdf(PDF_PATH)
    print(f"Loaded {len(docs)} pages from {PDF_PATH}")

    chunks = chunk_documents(docs)

    create_vector_store(chunks)

    print(f"Total chunks created: {len(chunks)}")


if __name__ == "__main__":
    main()
