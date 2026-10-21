from langchain_groq import ChatGroq

from app.config.settings import settings

def create_llm() -> ChatGroq:
    ## Create and return the application's LLM instance

    return ChatGroq(
        model=settings.llm_model,
        temperature=settings.llm_temperature,
        api_key=settings.groq_api_key
    )