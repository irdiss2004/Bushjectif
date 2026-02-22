
from ssl import _PasswordType
from fastapi import HTTPException
from models.users import User 
from database import SessionLocal as Session






def register(db:Session , create_user:User):
    existing_user=db.query(User).filter(User.user_name == create_user.user_name).first()
    if existing_user:
        raise HTTPException(status_code=400 , detail={"message": "User already exists"})
    user=User(
    user_name=create_user.user.user_name,
    password = create_user.password,
    description= create_user.description 
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user



def login(db: Session , connection_user:User):
    user=db.query(User).filter( User.password==connection_user.password , User.user_name==connection_user.user_name).first()
    
    if not user:
        raise HTTPException(status_code=401 , detail={"message":"user not found"})
    if user.password != connection_user.password:
        raise HTTPException(status_code = 400 , detail={"Invalid password"})
    return{"message":"success connection"}
    
def delete_account(db:Session, user_id:int):
    user=db.query(User).filter(User.id == user_id ).first()
    if not user:
        raise HTTPException(status_code=404 , detail={"message": "User not found"})
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}  


def get_user_profile (db:Session , user_id:int):  
    user=db.query(User).filter(User.id == user_id ).first()
    if not user :
        raise HTTPException(status_code=404 , detail = {"message": " user not found"})
    return{"message": "voici votre profils ", "user": user}