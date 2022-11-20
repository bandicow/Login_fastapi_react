import datetime
import pydantic


# API에서 보여주기 위한 정의 
class UserBase(pydantic.BaseModel):
    LoginID : str
    
class UserCreate(UserBase):
    hashed_password : str
    
    class Config:
        orm_mode = True


class User(UserBase):
    id : int
    
    class Config:
        orm_mode = True
