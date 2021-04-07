import data

from typing import List

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from models import Template

router = APIRouter(
    prefix="/templates",
    tags=["templates"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[Template])
async def read_templates():
    return [template for template in data.get_all_templates()]


@router.get("/{idx}", response_model=Template)
async def read_template_with_idx(idx: UUID):
    template = data.get_template(idx)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template


@router.post("/{idx}", response_model=Template)
async def add_template(idx: UUID, template: Template):
    data.add_template(template.dict())
    template = data.get_template(idx)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template


@router.delete(
    "/{idx}",
    response_model=List[Template],
)
async def delete_template_with_idx(idx: UUID):
    data.remove_template(idx)
    return [templates for templates in data.get_all_templates()]