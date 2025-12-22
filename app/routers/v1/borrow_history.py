from uuid import UUID
from fastapi import APIRouter, Query, Depends
from app.schemas.borrow_history import (
    BorrowHistoryCreateV1,
    BorrowHistoryUpdateV1,
    Response,
)

from app.dependencies import get_db
from sqlalchemy.orm import Session

borrow_history_router_v1 = APIRouter()


@borrow_history_router_v1.get(
    '/books/borrow_history/', status_code=200, response_model=Response
)
async def get_borrow_histories(
    sort: str = Query(...),
    offset: int = Query(...),
    limit: int = Query(...),
    db: Session = Depends(get_db),
):
    pass


@borrow_history_router_v1.get(
    '/books/borrow_history/{borrow_history_id}/',
    status_code=200,
    response_model=Response,
)
async def get_borrow_history(borrow_history_id: UUID, db: Session = Depends(get_db)):
    pass


@borrow_history_router_v1.post(
    '/books/borrow_history/', status_code=201, response_model=Response
)
async def create_borrow_history(
    borrow_history_create: BorrowHistoryCreateV1, db: Session = Depends(get_db)
):
    pass


@borrow_history_router_v1.patch(
    '/books/borrow_history/{borrow_history_id}/',
    status_code=200,
    response_model=Response,
)
async def update_borrow_history(
    borrow_history_id: UUID,
    borrow_history_update: BorrowHistoryUpdateV1,
    db: Session = Depends(get_db),
):
    pass


@borrow_history_router_v1.delete(
    '/books/borrow_history/{borrow_history_id}/', status_code=204
)
async def delete_borrow_history(borrow_history_id: UUID, db: Session = Depends(get_db)):
    pass
