"""Database functions"""

import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy

router = APIRouter()


async def get_db() -> sqlalchemy.engine.base.Connection:
    """Get a SQLAlchemy database connection.
    
    Uses this environment variable if it exists:  
    DATABASE_URL=dialect://user:password@host/dbname

    Otherwise uses a SQLite database for initial local development.
    """
    load_dotenv()
    database_url = os.getenv('DATABASE_URL', default='sqlite:///temporary.db')
    engine = sqlalchemy.create_engine(database_url)
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()


@router.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": f"Hello {item_id}!"}


@router.get('/info')
async def get_url(connection=Depends(get_db)):
    """Verify we can connect to the database, 
    and return the database URL in this format:

    dialect://user:password@host/dbname

    The password will be hidden with ***
    """
    url_without_password = repr(connection.engine.url)
    return {'database_url': url_without_password}

@router.get('/hello')
async def hello():
    """Returns a friendly greeting 👋"""
    return "Hello world"

from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@router.post("/items/")
async def create_item(item: Item):
    return item