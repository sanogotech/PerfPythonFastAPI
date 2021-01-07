from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}