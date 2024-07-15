from pydantic import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "TODO API"
    ROOT_PATH: str = "/"
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
