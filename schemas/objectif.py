


from pydantic import BaseModel

from .user import User


class Goal(BaseModel):

    id : int
    title :str
    objectif_quantify : int
    objectif_quantify_uniter :str
    user_id : int
    progretion : int
    date_creation:str
    count_update:int
    
    

class NewGoal (BaseModel):
    
    title :str
    objectif_quantify : int
    objectif_quantify_uniter :str
    user_id : int
    

class Update(BaseModel):
    progretion : int
    
