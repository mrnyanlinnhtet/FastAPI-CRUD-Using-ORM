from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class UserRegister(BaseModel):
    id: Optional[UUID4] = None
    name: str
    email: str
    password: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()


class UserLogin(BaseModel):
    email: str
    password: str