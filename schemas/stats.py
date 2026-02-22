from pydantic import BaseModel
from .user import User


c


class Recap(BaseModel):
    
    all_objectif: int
    doing: int
    progretion:int
    activity_day : int
    in_process: int
    


class CompactView(BaseModel):
    percent_complete:str
    percent_in_progress: int



class ProgressByObjective(BaseModel):
    objective_id: int
    progress: int
    
    
    
    



