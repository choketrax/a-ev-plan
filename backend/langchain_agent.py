from langchain.llms import OpenAI

llm = OpenAI(temperature=0.7)

def get_ai_response(prompt: str) -> str:
    return llm(prompt)
