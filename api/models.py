from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    id: Optional[int] = None
    column1: Optional[str] = None
    column2: str
