from typing import Optional
from uuid import UUID, uuid4
from fastapi import Query
from pydantic import BaseModel, Field


class Template(BaseModel):
    id: Optional[str] = ""
    idx: UUID = Field(default_factory=uuid4)
    thumbnail: Optional[str] = ""
    template: Optional[bool] = False
    assets: Optional[str] = Query("", alias="gjs-assets")
    html: Optional[str] = Query("", alias="gjs-html")
    css: Optional[str] = Query("", alias="gjs-css")
    components: Optional[str] = Query("", alias="gjs-components")
    styles: Optional[str] = Query("", alias="gjs-styles")


class Asset(BaseModel):
    id: Optional[int] = None
    url: str