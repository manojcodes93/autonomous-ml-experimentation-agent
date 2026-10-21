from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

## Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

## Loading env variables from .env
load_dotenv(BASE_DIR/".env")

class Settings(BaseSettings):
    """Application-wide config"""

    groq_api_key: str
    llm_model: str = "llama-3.3-70b-versatile"
    llm_temperature: float = 0.0
    database_path: str = "data/analyst.duckdb"

settings = Settings()