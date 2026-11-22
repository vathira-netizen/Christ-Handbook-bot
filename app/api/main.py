from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

from app.retrieval.history_aware import rewrite_question
from app.retrieval.retriever import retrieve_docs
from app.retrieval.reranker import rerank
from app.generation.generator import generate_answer

app = FastAPI(
    title="Christ University Handbook Bot",
    description="Conversational RAG assistant that answers questions "
                "grounded in the Christ University student handbook.",
    version="1.0.0"
)

chat_history = []

class QueryRequest(BaseModel):
    question: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/ask")
def ask_question(request: QueryRequest):

    question = request.question

    history_text = "\n".join(chat_history)

    standalone_question = rewrite_question(
        history_text,
        question
    )

    docs = retrieve_docs(standalone_question)

    ranked_docs = rerank(
        standalone_question,
        docs
    )

    context = "\n\n".join([
        doc.page_content
        for doc in ranked_docs[:3]
    ])

    answer = generate_answer(
        context,
        history_text,
        question
    )

    chat_history.append(f"User: {question}")
    chat_history.append(f"Assistant: {answer}")

    return {
        "question": question,
        "standalone_question": standalone_question,
        "answer": answer
    }
