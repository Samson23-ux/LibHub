from uuid import UUID
from fastapi import APIRouter, Query
from app.schemas.penalties import PenaltyCreateV1, PenaltyUpdateV1, Response

penalty_router_v1 = APIRouter()


@penalty_router_v1.get(
    '/penalties/', status_code=200,
    response_model=Response
)
async def get_penalties(
    sort: str = Query(...),
    offset: int = Query(...),
    limit: int = Query(...)
):
    pass


@penalty_router_v1.get(
    '/penalties/{penalty_id}/',
    status_code=200,
    response_model=Response
)
async def get_penalty(penalty_id: UUID):
    pass


@penalty_router_v1.post(
    '/penalties/',
    status_code=201,
    response_model=Response
)
async def create_penalty(penalty_create: PenaltyCreateV1):
    pass


@penalty_router_v1.patch(
    '/penalties/{penalty_id}/',
    status_code=200,
    response_model=Response
)
async def update_penalty(penalty_id: UUID, penalty_update: PenaltyUpdateV1):
    pass


@penalty_router_v1.delete(
    '/penalties/{penalty_id}/',
    status_code=204
)
async def delete_penalty(penalty_id: UUID):
    pass