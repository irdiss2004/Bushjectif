from pydantic import BaseModel

from models import objectif


class goal_dashboard(BaseModel):
    title :str
    statut:str
    total_moyenne: int
    user_moyenne: int
    comt_update : int
    date_creation:str
    
    
    
    
