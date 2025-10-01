from fastapi import Depends, HTTPException, APIRouter, status
from app.schemas.user_schemas import UserRegister, UserLogin
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.service import user_service
from app.utils.password import verify
from app.utils.authentication import generate_jwt_token


router = APIRouter(prefix="")

@router.post("/register")
async def register(user: UserRegister, db: AsyncSession=Depends(get_db)):
    """Handle user registration."""
    existing_user = await user_service.get_user_by_email(db, user.email)

    if existing_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already registered.")
    else:
        token_data = {
            "email": existing_user.email,
            "name": existing_user.name
        }
        token = generate_jwt_token(token_data)
        await user_service.user_registration(db, user)
        return {
               "message": "Successfully registered",
               "token": token
               }


@router.post("/login")
async def login(user: UserLogin, db: AsyncSession=Depends(get_db)):
    """Handle user login."""
    existing_user = await user_service.get_user_by_email(db, user.email)

    if not existing_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    if not verify(user.password, existing_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token_data = {
            "id": str(existing_user.id),
            "email": existing_user.email,
            "name": existing_user.name
            }
    token = generate_jwt_token(token_data)
    return {
           "message": "User login success",
           "token": token
           }

