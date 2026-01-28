from pydantic_settings import BaseSettings  # pip install pydantic-settings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()