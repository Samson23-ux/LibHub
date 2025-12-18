import uuid
import enum
from datetime import datetime
from app.database.base import Base

from sqlalchemy import (
    Column,
    VARCHAR,
    Integer,
    DateTime,
    Boolean,
    UUID,
    Enum,
    Text
)


class Role(str, enum.Enum):
    USER: str = 'user'
    LIBRARIAN: str = 'librarian'
    ADMIN: str = 'admin'


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    fullname = Column(VARCHAR(50), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    email = Column(VARCHAR(50), nullable=False, unique=True, index=True)
    password = Column(Text, nullable=False)
    nationality = Column(VARCHAR(50), nullable=False)
    role = Column(Enum(Role), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
    delete_at = Column(DateTime)
    email_remainder_at = Column(DateTime)

