from fastapi import APIRouter

router = APIRouter()


@router.get('/hello')
async def hello():
    """Returns a friendly greeting 👋"""
    return {"messsage": "Hello World!"}


