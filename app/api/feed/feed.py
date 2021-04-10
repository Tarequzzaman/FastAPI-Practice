from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, Request
from app.db.fetch_data import fetch
from app.sql.questions import questoions
from fastapi_pagination import LimitOffsetPage, Page, add_pagination
from fastapi_pagination.ext.asyncpg import paginate

router = APIRouter()


@router.get("/")
async def hello_world():
    """Hello world for this app 
       just visit the base path and see the function output

    Returns:
        Object: The function return hellow world object
    """
    return {"status": "success"}



@router.get("/questions/")
async def read_users(request : Request):
    """[summary]

    Args:
        request (Request): [description]

    Returns:
        [type]: [description]
    """
    data = await fetch(request.app.state.db, questoions)
    return data






 
