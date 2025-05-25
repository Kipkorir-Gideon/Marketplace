from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, utils
from .database import get_db

router = APIRouter()

@router.post("/register", response_model=models.User)
def register_user(user: models.UserCreate, db: Session = Depends(get_db)):
    db_user = utils.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return utils.create_user(db=db, user=user)

@router.post("/login")
def login_user(user: models.UserLogin, db: Session = Depends(get_db)):
    db_user = utils.authenticate_user(db, email=user.email, password=user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": utils.create_access_token(data={"sub": db_user.email}), "token_type": "bearer"}

@router.get("/{user_id}", response_model=models.User)
def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    user = utils.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=models.User)
def update_user_profile(user_id: int, user: models.UserUpdate, db: Session = Depends(get_db)):
    db_user = utils.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return utils.update_user(db=db, user_id=user_id, user=user)

@router.post("/refresh-token")
def refresh_token(token: str):
    return utils.refresh_access_token(token)