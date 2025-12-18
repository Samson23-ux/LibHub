from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


database_url: str = settings.DATABASE_URL
db_engine: Engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
