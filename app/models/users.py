import uuid
import enum
from datetime import datetime
from app.database.base import Base

from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    VARCHAR,
    Integer,
    DateTime,
    Boolean,
    UUID,
    Enum,
    Text,
    ForeignKey,
)


class UserRole(str, enum.Enum):
    ADMIN: str = "admin"
    LIBRARIAN: str = "librarian"
    USER: str = "user"


class TokenStatus(str, enum.Enum):
    VALID: str = 'valid'
    USED: str = 'used'
    REVOKED: str = 'revoked'


class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    fullname = Column(VARCHAR(50), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    email = Column(VARCHAR(50), nullable=False, unique=True, index=True)
    password = Column(Text, nullable=False)
    nationality = Column(VARCHAR(50), nullable=False)
    role_id = Column(UUID, ForeignKey("roles.id", ondelete="SET NULL"), index=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
    delete_at = Column(DateTime)
    email_remainder_at = Column(DateTime)

    borrow_histories = relationship(
        "BorrowHistory",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    role = relationship("Role", back_populates="users")

class Role(Base):
    __tablename__ = "roles"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    name = Column(Enum(UserRole), nullable=False)

    users = relationship("User", back_populates="role", passive_deletes=True)


class RefreshToken(Base):
    __tablename__ = 'refresh_tokens'

    id = Column(UUID, primary_key=True)
    user_id = Column(VARCHAR(50), nullable=False)
    token = Column(Text, nullable=False)
    status = Column(Enum(TokenStatus), default=TokenStatus.VALID, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    used_at = Column(DateTime)
    revoked_at = Column(DateTime)
