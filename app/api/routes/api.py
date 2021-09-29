from fastapi import APIRouter
from app.api.feed import feed
router = APIRouter()
router.include_router(feed.router)
