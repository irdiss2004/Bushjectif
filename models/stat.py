
from sqlalchemy  import Column , Integer , String
from database import Base


class Stat (Base):
    __tablename__ = "stat"
    
    all_objectif = column(Iteger , default =0)
    doing = column(Iteger , default =0)
    progretion = column(Iteger , default =0)
    activity_day = column(Iteger , default =0)
    in_process = column(Iteger , default =0)
    percent_complete = column(String , default =0)
    percent_in_progress = column(String , default =0)
    objective_id = column(Integer , default =0)
    







