from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from service import dashboard
from schemas.dashboard import goal_dashboard


router = APIRouter(prefix="/dashboard" , tags = ["dashboard goal"]) 

@router.get("/dasboard_goal", response_model=list[goal_dashboard])
def get_dashbord_goal(user_id: int , db:Session = Depends(get_db)):
    return dashboard.get_dashbord_goal(db, user_id)
