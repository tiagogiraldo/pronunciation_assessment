from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

def generate_sentences(topic, n=1):
    prompt = ChatPromptTemplate.from_template(
        "You are a helpful assistant. Generate exactly {n} simple sentences about the topic: {topic}. "
        "Each sentence must be in English and appropriate for all audiences. "
        "Return each sentence on a new line without any numbering or bullets"
    )
    model = OllamaLLM(model="gemma3n:e2b")  # or any model you have
    chain = prompt | model | StrOutputParser()
    response = chain.invoke({"topic": topic, "n": n})
    sentences = [s.strip() for s in response.splitlines() if s.strip()]
    return sentences[:n]