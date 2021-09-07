from typing import Optional
from uuid import UUID, uuid4
from fastapi import Query
from pydantic import BaseModel, Field

from constants import GJS_PREFIX


class Template(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: Optional[str] = ""
    thumbnail: Optional[str] = ""
    template: Optional[bool] = False
    description: Optional[str] = ""
    assets: Optional[str] = Query("", alias=f"{GJS_PREFIX}assets")
    pages: Optional[str] = Query("", alias=f"{GJS_PREFIX}pages")
    styles: Optional[str] = Query("", alias=f"{GJS_PREFIX}styles")
    updated_at: Optional[str] = ""


class Asset(BaseModel):
    id: Optional[int] = None
    url: str