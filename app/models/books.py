import uuid
import enum
from app.database.base import Base

from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    VARCHAR,
    Text,
    Integer,
    Date,
    UUID,
    Enum,
    ForeignKey,
    UniqueConstraint
)


class Status(str, enum.Enum):
    AVALAIBLE: str = 'available'
    OUT_OF_STOCK: str = 'out_of_stock'


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
        'Author',
        secondary='BookAuthor',
        back_populates='books'
    )


    genres = relationship(
        'Genre',
        secondary='BookGenre',
        back_populates='books'
    )


class Author(Base):
    __tablename__ = 'authors'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    fullname = Column(VARCHAR(50), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    email = Column(VARCHAR(50), nullable=False, unique=True, index=True)
    nationality = Column(VARCHAR(50), nullable=False)


    books = relationship(
        'Book',
        secondary='BookAuthor',
        back_populates='authors'
    )


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    name = Column(VARCHAR(50), nullable=False, index=True)
    age_rating = Column(Integer, nullable=False)

    books = relationship(
        'Book',
        secondary='BookGenre',
        back_populates='genres'
    )


class BookGenre(Base):
    __tablename__ = 'book_genre'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    book_id = Column(UUID, ForeignKey('books.id'), nullable=False)
    genre_id = Column(UUID, ForeignKey('genres.id'), nullable=False)

    __table_args__ = UniqueConstraint('book_id', 'genre_id')


class BookAuthor(Base):
    __tablename__ = 'book_author'

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    book_id = Column(UUID, ForeignKey('books.id'), nullable=False)
    author_id = Column(UUID, ForeignKey('authors.id'), nullable=False)

    __table_args__ = UniqueConstraint('book_id', 'author_id')
