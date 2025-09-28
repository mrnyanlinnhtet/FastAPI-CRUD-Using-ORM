from app.model.user_model import Users
from app.schemas.user_schemas import UserRegister, UserLogin
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException


async def user_registration(db: AsyncSession, user: UserRegister):
    """Create user from user registration."""
    user_obj = Users(**user.model_dump())
    db.add(user_obj)
    await db.commit()
    await db.refresh(user_obj)
    return user_obj



async def get_user_by_email(db: AsyncSession, email: str):
    """Get user by email."""
    result = await db.execute(select(Users).where(Users.email == email))
    user_obj = result.scalar_one_or_none()
    if user_obj:
        return user_obj
    else:
        HTTPException(status_code=404, detail="User not found!")