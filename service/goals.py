
from models import objectif
from schemas.objectif import NewGoal , Update
from fastapi import HTTPException
from models.users import User
from sqlalchemy.orm import Session
from models.Goal import Goal





def new_objectif(db:Session , goal_new:NewGoal):
    user = db.query(User).filter(User.id == goal_new.user_id).first()   #query pour dire requette donc db.query(User)pour dire demande de requette a ma base de donner pour la table user
    if not user:
        raise HTTPException(status_code=404 , detail={"message": "User not found"})
    
    
    goal= Goal(
        title=goal_new.title,
        objectif_quantify = goal_new.objectif_quantify, 
        objectif_quantify_uniter=goal_new.objectif_quantify_uniter,
        user_id=goal_new.user_id,
        progretion = 0,
        date_creation=None,
        count_update=0
    )
    db.add(goal)
    db.commit()
    db.refresh(goal)
    return goal

def update_opjectif(db:Session , goal_update: Update):
    goal = db.query(Goal).filter(Goal.id==goal_update.id).first()
    
    if not goal:
        raise HTTPException(status_code = 404 , detail={"message":"objectif not found"})
    goal.progretion=goal_update.progretion    
    
    goal.progretion += goal.progretion
    goal.count_update += 1
    
    db.commit()
    db.refresh(goal)
    return goal


def get_objectif(db:Session , goal_id:int):
    goal = db.query(Goal).filter(Goal.id == goal_id).first()
    return goal
