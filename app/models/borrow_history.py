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
    VARCHAR,
    Integer,
    UniqueConstraint,
)


class Status(str, enum.Enum):
    APPROVED: str = 'approved'
    BORROWED: str = 'borrowed'
    DENIED: str = 'denied'
    OVERDUE: str = 'overdue'
    PENDING: str = 'pending'
    RETURNED: str = 'returned'


class BorrowHistory(Base):
    __tablename__ = 'borrow_histories'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    user_id = Column(UUID, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    admin_id = Column(UUID, ForeignKey('users.id', ondelete='SET NULL'))
    staff_id = Column(UUID, ForeignKey('users.id', ondelete='SET NULL'), nullable=False)
    request_date = Column(DateTime, default=datetime.now(), nullable=False)
    borrow_date = Column(DateTime)
    due_date = Column(DateTime)
    return_date = Column(DateTime)
    status = Column(Enum(Status), default=Status.PENDING, nullable=False)

    penalty = relationship(
        'Penalty', back_populates='borrow_history', uselist=False, passive_deletes=True
    )

    user = relationship('User', back_populates='borrow_histories')

    borrow_items = relationship(
        'BorrowItem',
        back_populates='borrow_history',
        passive_deletes=True,
        cascade='all, delete-orphan',
    )


class BorrowItem(Base):
    __tablename__ = 'borrow_items'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    borrow_id = Column(
        UUID, ForeignKey('borrow_histories.id', ondelete='CASCADE'), unique=True
    )
    book_id = Column(UUID, ForeignKey('books.id', ondelete='SET NULL'), unique=True)
    quantity = Column(Integer, nullable=False)

    book = relationship('Book', back_populates='borrow_items')
    borrow_history = relationship('BorrowHistory', back_populates='borrow_items')

    __table_args__ = UniqueConstraint('borrow_id', 'book_id')


class Penalty(Base):
    __tablename__ = 'penalties'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    borrow_id = Column(
        UUID,
        ForeignKey('borrow_histories.id', ondelete='CASCADE'),
        unique=True,
        nullable=False,
    )
    description = Column(VARCHAR(50), nullable=False)
    fine = Column(Numeric(5, 2), nullable=False)

    borrow_history = relationship('BorrowHistory', back_populates='penalty')

    __table_args__ = UniqueConstraint('borrow_id')
