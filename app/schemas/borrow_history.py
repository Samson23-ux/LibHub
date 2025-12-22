from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, Any
from enum import Enum
from uuid import UUID


class Status(str, Enum):
    APPROVED: str = 'approved'
    BORROWED: str = 'borrowed'
    DENIED: str = 'denied'
    OVERDUE: str = 'overdue'
    PENDING: str = 'pending'
    RETURNED: str = 'returned'


class BorrowHistoryBaseV1(BaseModel):
    book_title: str
    quantity: int
    full_name: str
    admin: Optional[str] = None
    librarian: str
    due_date: Optional[datetime] = None
    status: Optional[Status] = None


class BorrowHistoryInDBV1(BorrowHistoryBaseV1):
    id: UUID
    request_date: Optional[datetime] = None
    borrow_date: Optional[datetime] = None
    return_date: Optional[datetime] = None


class BorrowHistoryCreateV1(BorrowHistoryBaseV1):
    pass


class BorrowHistoryUpdateV1(BaseModel):
    book_title: Optional[str] = None
    quantity: Optional[int] = None
    user_name: Optional[str] = None
    admin: Optional[str] = None
    librarian: Optional[str] = None
    request_date: Optional[datetime] = None
    borrow_date: Optional[datetime] = None
    due_date: Optional[datetime] = None
    return_date: Optional[datetime] = None
    status: Optional[Status] = None


class Response(BaseModel):
    message: Optional[str] = None
    data: Any
