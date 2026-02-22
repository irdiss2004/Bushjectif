from fastapi import APIRouter, Depends
from schemas.stats import Recap , CompactView,ProgressByObjective
from service.statistic import get_summarys,get_overviews
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/stats", tags=["statistique utilisateur"])


@router.get("/summary" , response_model=list[Recap])
def get_summary(user_id:int,  db: Session = Depends(get_db)):
    
    return get_summarys.get_summary(db,user_id)






@router.get("/overview", response_model=list[CompactView])
def get_overview(user_id:int , db:Session= Depends(get_db)):
    return get_overviews.get_overview (db , user_id)





@router.get("/progress", response_model=list[ProgressByObjective])
def get_progress_by_objective(user_id: int, db: Session= Depends(get_db)):
    return statistic.get_progress_by_objective(db , user_id)
