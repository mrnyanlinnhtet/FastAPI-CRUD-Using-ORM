from fastapi import Depends, HTTPException, APIRouter, status
from app.model.user_model import Users
from app.schemas.user_schemas import UserRegister, UserLogin
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.service import user_service


routers = APIRouter(prefix="")

@routers.post("/register")
async def register(user: UserRegister, db: AsyncSession=Depends(get_db)):
    """User registration process"""
    existing_user = await user_service.get_user_by_email(db, user.email)

    if existing_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already registered.")
    else:
        await user_service.user_registration(db, user)
        return {"message": "Successfully registered"}


@routers.post("/login")
async def login(user: UserLogin, db: AsyncSession=Depends(get_db)):
    """User login process"""
    existing_user = await user_service.get_user_by_email(db, user.email)

    if existing_user is None or (user.password != existing_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {"message": "User login success"}

