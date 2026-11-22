import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from app.generation.prompts import RAG_PROMPT

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
    temperature=0
)

def generate_answer(context, history, question):

    prompt = RAG_PROMPT.format(
        context=context,
        history=history,
        question=question
    )

    response = llm.invoke(prompt)

    return response.content