import data

from typing import List

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from models import Template
from utils.tasks import prefix

router = APIRouter(
    prefix="/templates",
    tags=["templates"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[Template])
async def read_templates():
    return [prefix(template) for template in data.get_all_templates()]


@router.get("/{id}", response_model=Template)
async def read_template_with_id(id: UUID):
    template = data.get_template(id)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return prefix(template)


@router.post("/{id}", response_model=Template)
async def add_template(id: UUID, template: Template):
    data.add_template(template.dict())
    template = data.get_template(id)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return prefix(template)


@router.delete(
    "/{id}",
    response_model=List[Template],
)
async def delete_template_with_id(id: UUID):
    data.remove_template(id)
    return [prefix(template) for template in data.get_all_templates()]