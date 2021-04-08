from typing import Optional

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def hello_world():
    return {"status": "success"}


@router.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]