from uuid import UUID
from fastapi import APIRouter, Query
from app.schemas.books import BookCreateV1, BookUpdateV1, Response

book_router_v1 = APIRouter()


@book_router_v1.get('/books/', status_code=200, response_model=Response)
async def get_books(
    sort: str = Query(...),
    offset: int = Query(...),
    limit: int = Query(...)
):
    pass


@book_router_v1.get('/books/{book_id}/', status_code=200, response_model=Response)
async def get_book(book_id: UUID):
    pass


@book_router_v1.post('/books/', status_code=201, response_model=Response)
async def create_book(user_create: BookCreateV1):
    pass


@book_router_v1.patch('/books/{book_id}/', status_code=200, response_model=Response)
async def update_book(book_id: UUID, user_update: BookUpdateV1):
    pass


@book_router_v1.delete('/books/{book_id}/', status_code=204)
async def delete_book(book_id: UUID):
    pass
