from pydantic import BaseSettings


class Settings(BaseSettings):
    intents_file: str
    model_trained_file: str
    bot_name: str

    class Config:
        env_file = ".env"


settings = Settings()
