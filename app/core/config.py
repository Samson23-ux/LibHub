from datetime import datetime
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    API_TITLE: str = 'Library API'
    API_VERSION_1: str = '/api/v1'
    DESCRIPTION: str = 'A REST API for a Library Management System'

    DATABASE_URL: str

    ACCESS_TOKEN_EXPIRE_MINUTES: datetime = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: datetime = 30
    TOKEN_ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_SECRET_KEY: str
    REFRESH_TOKEN_SECRET_KEY: str

    class config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
