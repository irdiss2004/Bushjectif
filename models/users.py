from contextlib import nullcontext

from sqlalchemy  import Column , Integer , String
from database import Base


class User(Base):
    __tablename__= "users"
    
    id= Column(Integer , primary_key = True , index = True )
    user_name= Column (String, nullable= False )
    note= Column(Integer , default=0)
    password= Column(String, nullable= False)
    
    
    
    
