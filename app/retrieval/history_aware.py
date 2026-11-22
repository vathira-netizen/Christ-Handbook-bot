import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
    temperature=0
)

template = """
Given the conversation history and latest question,
rewrite the latest question into a standalone question.

Chat History:
{history}

Question:
{question}

Standalone Question:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["history", "question"]
)

def rewrite_question(history, question):

    formatted_prompt = prompt.format(
        history=history,
        question=question
    )

    response = llm.invoke(formatted_prompt)

    return response.content