from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from service import  goals  
from schemas.objectif import  NewGoal , Update




router = APIRouter(prefix="/objectif", tags= ["definir les objectifs"] )

@router.post("/new_objectif")
def creat_goal( goal_new: NewGoal, db: Session = Depends(get_db)):
    return goals.new_objectif (db , goal_new) 

@router.put("/update_goal")
def update_goal( goal_update: Update, db: Session = Depends(get_db) ):
    return goals.update_objectif(db ,goal_update)


@router.get("/get_all_goals")
def get_all_goals(user_id:int ,db: Session = Depends(get_db)):
    return goals.get_all_goals(db,user_id)

