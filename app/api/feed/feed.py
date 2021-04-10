from typing import Optional

from fastapi import APIRouter, Request
from app.db.fetch_data import fetch
from app.db.sql.questions import questoions


router = APIRouter()


@router.get("/")
async def hello_world():
    return {"status": "success"}


@router.get("/questions/")
async def read_users(request : Request):
    data = await fetch(request.app.state.db, questoions)
    return data