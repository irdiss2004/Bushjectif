
from pydantic import BaseModel


class User(BaseModel):
    user_id :int
    User_name :str
    password :str 
    description : str | None = None # type: ignore
    
    
class UserCreate(BaseModel):
    user_name: str
    password: str
    
    
class UserConnection(BaseModel):
    user_name: str
    password: str
    
    
    
    
    
    



