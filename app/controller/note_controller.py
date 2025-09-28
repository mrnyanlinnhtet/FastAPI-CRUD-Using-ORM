from fastapi import APIRouter

routers = APIRouter(prefix="/notes")


@routers.get("/")
async def test():
    return {"message": "note"}