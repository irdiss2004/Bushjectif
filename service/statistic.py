from fastapi import HTTPException
from models import Goal
from datatime import datetime



existing_goal= db.query(Goal).filter(Goal.user_id == user_id).all()
total_count = len(existing_goal)
doing_count=sum(g for g in existing_goal if g.status == "doing")

def get_summarys(db:Session , user_id:int):
    existing_goal= db.query(Goal).filter(Goal.user_id == user_id).all()
    if not  existing_goal :
        raise HTTPException(status_code=404 , detail="Goal not found")
    
    first_star = min(g.created_at for ga in existing_goal)
    delta = datetime.now() -first_star

    in_process = f"{(total_count -doing_count) / total_count * 100 }%" 

    progretion =f"{(doing_count/total_count*100):.2f} %"
    
    
    return {
        "all_objectif": total_count,
        "doing": doing_count,
        "progretion":progretion ,
        "activity_day": f"{delta.days}" ,
        "in_process": in_process
    }


def get_overviews(db:Session , user_id:int):
    exysting_goal= db.query(Goal).filter(Goal.user_id == user_id).all()
    if not  exysting_goal :
        
        raise HTTPException(status_code=404 , detail="Goal not found")
    
    
    percent_complete = f"{doing_count / total_count * 100 }%"
    percent_in_progress = (total_count - doing_count) / 100
    
    
    return {"percent_complete": percent_complete,
        "percent_in_progress": percent_in_progress
    }



def get_progress_by_objectives(db: Session ,user_id:int):
    existing_goal=db.query(Goal).filter(Goal.user_id == user_id).all()
    if not existing_goal:
        
    
        
        raise HTTPException(status_code=404 , detail="Goal not found")
    goal_progress_percent= []
    
    for g in existing_goal:
        # Calcul de la durée écoulée pour cet objectif spécifique
        delta = datetime.now() - g.created_at
        
        # Logique de pourcentage par objectif (à adapter selon vos champs)
        # Ici, on imagine que vous avez un champ 'progress' (int) dans votre base
        pourcentage = getattr(g, 'progress', 0) 
        
        # Si vous n'avez pas de champ progress, vous pouvez simuler :
        # pourcentage = 100 if g.status == "done" else 50 if g.status == "doing" else 0

        evolution_par_objectif.append({
            "goal_id": g.id,
            "title": g.title,
            "status": g.status,
            "progression": f"{pourcentage}%",
            "jours_actifs": delta.days
        })

    
    return{
        
        "goal_progress_percent": goal_progress_percent,
    }

    
    
    
    
    
