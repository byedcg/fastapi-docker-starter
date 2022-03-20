"""Keep pydantic models organized"""
from typing import Optional
from pydantic import BaseModel

# data model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
