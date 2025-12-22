import enum
from uuid import UUID
from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, EmailStr, ConfigDict


class UserRole(str, enum.Enum):
    ADMIN: str = "admin"
    LIBRARIAN: str = "librarian"
    USER: str = "user"

class UserBaseV1(BaseModel):
    full_name: str
    age: int
    email: EmailStr
    password: str
    nationality: str
    role: str


class UserCreateV1(UserBaseV1):
    pass


class UserInDBV1(UserBaseV1):
    id: UUID
    created_at: datetime
    is_deleted: bool
    delete_at: datetime
    email_remainder_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ReactivateAccountV1(BaseModel):
    full_name: str
    current_password: str


class UserUpdateV1(BaseModel):
    full_name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    nationality: Optional[str] = None
    role: Optional[str] = None


class PasswordUpdate(BaseModel):
    email: EmailStr
    currrent_password: str
    new_password: str


class Response(BaseModel):
    message: Optional[str] = None
    data: Any
