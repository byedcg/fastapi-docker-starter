from typing import Optional

from fastapi import APIRouter

router = APIRouter()


@router.get("/{message}")
async def echo(message: str, query: Optional[str] = None):
    return {"message": message, "query": query}
