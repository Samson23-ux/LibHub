from pydantic import BaseModel, ConfigDict
from typing import Optional, Any
from uuid import UUID


class PenaltyBaseV1(BaseModel):
    book_title: str
    description: str
    fine: int


class PenaltyInDBV1(PenaltyBaseV1):
    id: UUID
    borrow_id: UUID

    model_config = ConfigDict(from_attributes=True)


class PenaltyCreateV1(PenaltyBaseV1):
    pass


class PenaltyUpdateV1(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    fine: Optional[int] = None


class Response(BaseModel):
    message: Optional[str] = None
    data: Any
