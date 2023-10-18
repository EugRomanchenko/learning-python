from typing import Annotated

from fastapi import FastAPI, Query

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.get("/")
def hello_word():
    return {"message": "Hello Word!"}


@app.get("/hello/")
def hello_user(name: Annotated[str, Query(min_length=3)] = "User"):
    return {"message": f"Hello {name}"}


@app.get("/ping/")
def get_ping():
    return {"message": "pong"}


@app.put("/items/{item_id}")
def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
