import os

from pydantic import Field
from pydantic_settings import BaseSettings
from datetime import timedelta


class DatabaseSettings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    class Config:
        env_file = os.getenv("ENV_FILE", ".env")
        extra = "ignore"


class JWTSettings(BaseSettings):
    access_token_lifetime: int
    refresh_token_lifetime: int
    algorithm: str
    signing_key: str

    class Config:
        env_file = os.getenv("ENV_FILE", ".env")
        extra = "ignore"

class DjangoSettings(BaseSettings):
    secret_key: str
    debug: bool
    allowed_hosts: list[str]
    class Config:
        env_file = os.getenv("ENV_FILE", ".env")
        extra = "ignore"

class Settings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()
    jwt: JWTSettings = JWTSettings()
    django: DjangoSettings = DjangoSettings()


settings = Settings()
