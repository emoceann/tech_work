from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str

    class Config:
        env_file = 'dev.env'


def get_settings() -> Settings:
    return Settings()
