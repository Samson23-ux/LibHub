from pydantic import BaseModel, EmailStr,ConfigDict
from typing import Optional, Any
from uuid import UUID


class AuthorBaseV1(BaseModel):
    full_name: str
    age: int
    email: EmailStr
    nationality: str


class AuthorInDBV1(AuthorBaseV1):
    id: UUID

    model_config = ConfigDict(from_attributes=True)


class AuthorCreateV1(AuthorBaseV1):
    pass


class AuthorUpdateV1(BaseModel):
    full_name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    nationality: Optional[str] = None


class Response(BaseModel):
    message: Optional[str] = None
    data: Any
