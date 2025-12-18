from uuid import UUID
from app.schemas.penalties import (
    PenaltyV1,
    PenaltyCreateV1,
    PenaltyUpdateV1
)


class PenaltyService:
    async def get_penalties_v1(
            sort: str | None = None,
            offset: int = 0,
            limit: int = 0
    ) -> list[PenaltyV1]:
        pass


    async def get_penalty_v1(penalty_id: UUID) -> PenaltyV1:
        pass


    async def create_penalty_v1(
        penalty_create: PenaltyCreateV1
    ) -> PenaltyV1:
        pass


    async def update_penalty_v1(
        penalty_update: PenaltyUpdateV1,
        penalty_id: UUID
    ) -> PenaltyV1:
        pass


    async def delete_penalty_v1(penalty_id: UUID):
        pass

penalty_service = PenaltyService()