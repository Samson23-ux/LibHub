from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    API_TITLE: str = 'Library API'
    API_VERSION_1: str ='/api/v1'
    DESCRIPTION: str = 'A REST API for a Library Management System'

    DATABASE_URL: str

    class config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
