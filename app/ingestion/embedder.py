import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

def create_vector_store(chunks):

    embedding_model = OpenAIEmbeddings(
        model=os.getenv("EMBEDDING_MODEL")
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=os.getenv("CHROMA_DB_DIR")
    )

    # langchain-chroma persists automatically when persist_directory is set
    print("Vector DB created successfully!")

    return vectordb