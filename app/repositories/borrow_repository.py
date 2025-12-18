from uuid import UUID
from app.schemas.borrow_history import (
    BorrowHistoryV1,
    BorrowHistoryCreateV1,
    BorrowHistoryUpdateV1
)


class BorrowHistoryRepo:
    async def get_borrow_histories_v1(
            sort: str | None = None,
            offset: int = 0,
            limit: int = 0
    ) -> list[BorrowHistoryV1]:
        pass


    async def get_borrow_history_v1(borrow_history_id: UUID) -> BorrowHistoryV1:
        pass


    async def create_borrow_history_v1(
        borrow_history_create: BorrowHistoryCreateV1
    ) -> BorrowHistoryV1:
        pass


    async def update_borrow_history_v1(
        borrow_history_update: BorrowHistoryUpdateV1,
        borrow_history_id: UUID
    ) -> BorrowHistoryV1:
        pass


    async def delete_borrow_history_v1(borrow_history_id: UUID):
        pass


borrow_history_repo = BorrowHistoryRepo()
