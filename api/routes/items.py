import data

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from models import Item

router = APIRouter(
    prefix="/items", tags=["items"], responses={404: {"description": "Not found"}}
)


@router.get("", response_model=List[Item])
async def read_items():
    return [items for items in data.get_all_items()]


@router.get("/{column1}", response_model=Item)
async def read_item(column1: str):
    column2 = data.get_item(column1)
    if not column2:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"column1": column1, "column2": column2}


@router.post("", response_model=Item)
async def add_item(item: Item):
    data.add_item(
        item.column1,
        item.column2,
    )
    column2 = data.get_item(column1)
    if not column2:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"column1": column1, "column2": column2}


@router.delete(
    "",
    response_model=List[Item],
)
async def delete_item(item: Item):
    data.remove_item(
        item.column1,
        item.column2,
    )
    return [items for items in data.get_all_items()]