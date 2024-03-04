from app import app
from fastapi import APIRouter,HTTPException
from schemas.auth_routes import UserSignUp
from models.user import (User,serial)
from config.database import user_collection
router = APIRouter(prefix='/auth')



@router.post("/register")
async def root(user:UserSignUp):
    new_user = User(name=user.name, email=user.email, password=user.password, mobile_num=user.mobile_num)
    insert_result = user_collection.insert_one(dict(new_user))
    inserted_id = insert_result.inserted_id
    inserted_user = user_collection.find_one({'_id': inserted_id})
    return serial(inserted_user)

  