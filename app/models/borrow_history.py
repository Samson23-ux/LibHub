import uuid
import enum
from datetime import datetime
from app.database.base import Base


from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    DateTime,
    UUID,
    ForeignKey,
    Enum,
    Numeric,
    VARCHAR
)


class Status(str, enum.Enum):
    BORROWED: str = 'borrowed'
    RETURNED: str = 'returned'
    OVERDUE: str = 'overdue'


class BorrowHistory(Base):
    __tablename__ = 'borrow_histories'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    book_id = Column(UUID, ForeignKey('books.id'), nullable=False)
    user_id = Column(UUID, ForeignKey('users.id'), nullable=False)
    staff_id = Column(UUID, ForeignKey('staff.id'), nullable=False)
    borrow_date = Column(DateTime, default=datetime.now(), nullable=False)
    due_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, default=datetime.now())
    status = Column(Enum(Status), default=Status.BORROWED, nullable=False)


class Penalty(Base):
    __tablename__ = 'penalties'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    borrow_id = Column(UUID, ForeignKey('borrow_histories.id'), unique=True, nullable=False)
    description = Column(VARCHAR(50), nullable=False)
    fine = Column(Numeric(5, 2), nullable=False)

    borrow_history = relationship('BorrowHistory')
