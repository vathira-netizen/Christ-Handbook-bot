import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

embedding_model = OpenAIEmbeddings(
    model=os.getenv("EMBEDDING_MODEL")
)

vectordb = Chroma(
    persist_directory=os.getenv("CHROMA_DB_DIR"),
    embedding_function=embedding_model
)

retriever = vectordb.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": 5
    }
)

def retrieve_docs(query):

    docs = retriever.invoke(query)

    return docs