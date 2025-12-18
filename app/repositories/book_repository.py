from uuid import UUID
from app.schemas.books import BookV1, BookCreateV1, BookUpdateV1

class BookRepo:
    async def get_books_v1(
            sort: str | None = None,
            offset: int = 0, 
            limit: int = 0
    ) -> list[BookV1]:
        pass

    async def get_book_v1(book_id: UUID) -> BookV1:
        pass

    async def create_book_v1(book_create: BookCreateV1) -> BookV1:
        pass

    async def update_book_v1(book_update: BookUpdateV1, book_id: UUID) -> BookV1:
        pass

    async def delete_book_v1(book_id: UUID):
        pass

book_repo = BookRepo()