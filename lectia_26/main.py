from fastapi import FastAPI, HTTPException
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel


app = FastAPI(title='my first api', version='1.0.0')

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool= True 


items_db = []
next_id = 1

from fastapi import Header
from typing import Optional

@app.get("/items/")
def read_items(
    user_agent: Optional[str] = Header(None),
    x_token: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None, alias="Accept-Language")
):
    return {
        "User-Agent": user_agent,
        "X-Token": x_token,
        "Accept-Language": accept_language
    }


from fastapi import Cookie, Response
from typing import Optional

@app.get("/items/")
def read_items(
    session_id: Optional[str] = Cookie(None),
    user_preference: Optional[str] = Cookie(None, alias="user-preference"),
    theme: str = Cookie("light")
):
    return {
        "session_id": session_id,
        "user_preference": user_preference,
        "theme": theme
    }

