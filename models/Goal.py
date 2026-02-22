from sqlalchemy  import Column , Integer , String
from database import Base




class Goal (Base):
    __tablename__ = "Goals"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False, default=None)
    user_id = Column(Integer, nullable=False)
    objectif_quantify = Column(Integer, nullable=False)
    objectif_quantify_uniter = Column(String, nullable=False)
    progretion = Column(Integer, default=0)
    count_update =Column(Integer, default = 0)
    
    
    