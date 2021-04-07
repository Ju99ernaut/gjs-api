from typing import Optional
from uuid import UUID, uuid4
from fastapi import Query
from pydantic import BaseModel, Field

from constants import GJS_PREFIX


class Template(BaseModel):
    id: Optional[str] = ""
    idx: UUID = Field(default_factory=uuid4)
    thumbnail: Optional[str] = ""
    template: Optional[bool] = False
    assets: Optional[str] = Query("", alias=f"{GJS_PREFIX}assets")
    html: Optional[str] = Query("", alias=f"{GJS_PREFIX}html")
    css: Optional[str] = Query("", alias=f"{GJS_PREFIX}css")
    components: Optional[str] = Query("", alias=f"{GJS_PREFIX}components")
    styles: Optional[str] = Query("", alias=f"{GJS_PREFIX}styles")


class Asset(BaseModel):
    id: Optional[int] = None
    url: str