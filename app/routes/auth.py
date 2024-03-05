from app import app
from fastapi import APIRouter,HTTPException
from schemas.auth_routes import UserSignUp,UserLogin,ResponseWithToken
from models.user import (User,serial)
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from config.database import user_collection
from jose import JWTError, jwt
import bcrypt

router = APIRouter(prefix='/auth')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


class Bcrypts:
    @staticmethod
    def get_hash(password:str)->str:
        bytes = password.encode('utf-8') 
        salt = bcrypt.gensalt() 
        hash = bcrypt.hashpw(bytes, salt) 
        return hash
    
    @staticmethod
    def compare(password,hashed_password)->bool:
        return  bcrypt.checkpw(password.encode('utf-8'),hashed_password.encode('utf-8'))


@router.post("/sign-up")
async def sign_up(user:UserSignUp):
    '''
        This function is responsible for signing up a user with email and password
    '''

    hashed_password : str = Bcrypts.get_hash(user.password)
    new_user:User = User(name=user.name, email=user.email, password=hashed_password, mobile_num=user.mobile_num,created_datetime=datetime.utcnow(),updated_datetime=datetime.utcnow())
    existing_user = user_collection.find_one({'$or':[{'email':new_user.email},{'mobile_num':new_user.mobile_num}]})
    if existing_user:
        raise HTTPException(status_code=403,detail='User Already Exist')
    
    insert_result = user_collection.insert_one(dict(new_user))
    inserted_id = insert_result.inserted_id
    inserted_user = user_collection.find_one({'_id': inserted_id})
    inserted_user =  serial(inserted_user)
    
    access_token = create_access_token(data={'email':inserted_user['email'],'id':inserted_user['id']},expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return ResponseWithToken(user=inserted_user,access_token=access_token, token_type="bearer")


@router.post("/sign-in")
async def sign_in(user:UserLogin):
    '''
        This function is responsible for signing in a user with email and password
    '''

    db_user = user_collection.find_one({'email':user.email})
    if not db_user:
        raise HTTPException(status_code=404,detail='Enter valid credentials')
    hashed_password = db_user['password']
    db_user = serial(db_user)
    if Bcrypts.compare(user.password,hashed_password)==False:
        raise HTTPException(status_code=404,detail='Enter valid credentials')
    
    access_token = create_access_token(data={'email':db_user['email'],'id':db_user['id']},expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return ResponseWithToken(user=db_user,access_token=access_token, token_type="bearer")

    



  