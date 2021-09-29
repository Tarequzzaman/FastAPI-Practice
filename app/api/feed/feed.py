from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, Request
from app.db.fetch_data import fetch
from app.sql.questions import QUESTIONS
from fastapi_pagination import LimitOffsetPage, Page, add_pagination
from fastapi_pagination.ext.asyncpg import paginate

router = APIRouter()


@router.get("/")
async def hello_world():
    return {"status": "success"}

@router.get("/questions/")
async def read_users(request : Request):
    data = await fetch(request.app.state.db, QUESTIONS)
    return data
