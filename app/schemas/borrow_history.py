from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, Any
from enum import Enum
from uuid import UUID

class Status(str, Enum):
    borrowed: str = 'borrowed'
    returned: str = 'returned'
    overdue: str = 'overdue'

class BorrowHistoryBaseV1(BaseModel):
    book_title: str
    full_name: str
    staff_name: str
    due_date: datetime
    status: Optional[Status] = None

class BorrowHistoryInDBV1(BorrowHistoryBaseV1):
    id: UUID
    borrow_date: datetime
    return_date: Optional[datetime] = None

class BorrowHistoryCreateV1(BorrowHistoryBaseV1):
    pass

class BorrowHistoryUpdateV1(BaseModel):
    book_title: Optional[str] = None
    user_name: Optional[str] = None
    staff_name: Optional[str] = None
    borrow_date: Optional[datetime] = None
    due_date: Optional[datetime] = None
    return_date: Optional[datetime] = None
    status: Optional[Status] = None

class Response(BaseModel):
    message: Optional[str] = None
    data: Any
