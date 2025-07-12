from pydantic import BaseModel, EmailStr

# Input schema for registration
class UserCreate(BaseModel):
    id: str                # Helmet ID
    username: str
    email: EmailStr
    password: str

# Input schema for login
class UserLogin(BaseModel):
    username: str
    password: str

# Output schema for responses
class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr

    class Config:
        from_attributes = True  # updated name in Pydantic v2 (replaces orm_mode)
from typing import List
from pydantic import BaseModel

class ReadingInput(BaseModel):
    reading: List[float]  # [X, Y, Z, HR, TEMP]
    ch4_ppm: float
    co_ppm: float
