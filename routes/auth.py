

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate , UserConnection
from database import get_db
from service import users
router = APIRouter(prefix="/auth", tags=["authentification"]) 


@router.post("/register")
def register(user: UserCreate , db:Session = Depends(get_db)):
    return users.create_user(db,user)



@router.post("/login")
def login(user:UserConnection , db:Session = Depends(get_db)):
    db_user = users.get_user_by_username( db , user.user_name)
    
    if not db_user :
        raise HTTPException(status_code=404 , detail='User not found')


    if db_user.password != user.password:
        raise HTTPException(status_code = 400, detail= "Invalid password")
    
    return{"message":"your are connected"}


@router.delect("/revome_account")
def remouve_account(db:Session = Depends(get_user)):
    return {"message":"your account are deleted !  "}



