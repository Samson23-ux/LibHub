from pydantic import BaseModel, ConfigDict
from typing import Optional, Any
from enum import Enum
from uuid import UUID

class Status(str, Enum):
    available: str = 'available'
    out_of_stock: str = 'out_of_stock'

class BookBaseV1(BaseModel):
    title: str
    authors: list[str]
    genres: list[str]
    age_rating: int
    year_published: int
    isbn: str
    quantites: int
    description: Optional[str] = None
    status: Optional[Status] = None

class BookInDBV1(BookBaseV1):
    id: UUID

    model_config = ConfigDict(from_attributes=True)

class BookCreateV1(BookBaseV1):
    pass

class BookUpdateV1(BaseModel):
    title: Optional[str] = None
    authors: Optional[list[str]] = None
    genres: Optional[list[str]] = None
    age_rating: Optional[int] = None
    year_published: Optional[int] = None
    isbn: Optional[str] = None
    quantites: Optional[int] = None
    description: Optional[str] = None
    status: Optional[Status] = None

class Response(BaseModel):
    message: Optional[str] = None
    data: Any
