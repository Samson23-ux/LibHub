import uuid
import enum
from app.database.base import Base

from sqlalchemy import Table
from sqlalchemy.orm import relationship
from sqlalchemy import Column, VARCHAR, Text, Integer, Date, UUID, Enum, ForeignKey


class Status(str, enum.Enum):
    AVALAIBLE: str = 'available'
    OUT_OF_STOCK: str = 'out_of_stock'


book_author = Table(
    'book_authors',
    Base.metadata,
    Column('book_id', ForeignKey('books.id', ondelete='CASCADE'), primary_key=True),
    Column('author_id', ForeignKey('authors.id', ondelete='CASCADE'), primary_key=True),
)

book_genre = Table(
    'book_genres',
    Base.metadata,
    Column('book_id', ForeignKey('books.id', ondelete='CASCADE'), primary_key=True),
    Column('genre_id', ForeignKey('genres.id', ondelete='CASCADE'), primary_key=True),
)


class Book(Base):
    __tablename__ = 'books'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    title = Column(VARCHAR(50), unique=True, nullable=False, index=True)
    age_rating = Column(Integer, nullable=False)
    year_published = Column(Date, nullable=False)
    isbn = Column(Text, unique=True, nullable=False)
    description = Column(Text)
    quantities = Column(Integer, nullable=False)
    status = Column(Enum(Status), nullable=False, default=Status.AVALAIBLE)

    authors = relationship(
        'Author', secondary='book_author', back_populates='books', passive_deletes=True
    )

    genres = relationship(
        'Genre', secondary='book_genre', back_populates='books', passive_deletes=True
    )

    borrow_items = relationship(
        'BorrowItem', back_populates='book', passive_deletes=True
    )


class Author(Base):
    __tablename__ = 'authors'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    fullname = Column(VARCHAR(50), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    email = Column(VARCHAR(50), nullable=False, unique=True, index=True)
    nationality = Column(VARCHAR(50), nullable=False)

    books = relationship(
        'Book', secondary='book_author', back_populates='authors', passive_deletes=True
    )


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    name = Column(VARCHAR(50), nullable=False, index=True)
    age_rating = Column(Integer, nullable=False)

    books = relationship(
        'Book', secondary='book_genre', back_populates='genres', passive_deletes=True
    )
