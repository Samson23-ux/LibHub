from uuid import UUID
from fastapi import APIRouter, Query, Depends
from app.schemas.authors import AuthorCreateV1, AuthorUpdateV1, Response

from app.dependencies import get_db
from sqlalchemy.orm import Session

author_router_v1 = APIRouter()


@author_router_v1.get('/books/', status_code=200, response_model=Response)
async def get_authors(
    sort: str = Query(...),
    offset: int = Query(...),
    limit: int = Query(...),
    db: Session = Depends(get_db),
):
    pass


@author_router_v1.get('/books/{author_id}/', status_code=200, response_model=Response)
async def get_author(author_id: UUID, db: Session = Depends(get_db)):
    pass


@author_router_v1.post('/books/', status_code=201, response_model=Response)
async def create_author(author_create: AuthorCreateV1, db: Session = Depends(get_db)):
    pass


@author_router_v1.patch('/books/{author_id}/', status_code=200, response_model=Response)
async def update_author(
    author_id: UUID, author_update: AuthorUpdateV1, db: Session = Depends(get_db)
):
    pass


@author_router_v1.delete('/books/', status_code=204)
async def delete_author(author_id: UUID, db: Session = Depends(get_db)):
    pass
