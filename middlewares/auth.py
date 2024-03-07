from fastapi import HTTPException,Response,Request,Depends
from models.user import (serial)
from datetime import datetime, timedelta, timezone
from config.database import user_collection
from jose import JWTError, jwt
import os
from bson import ObjectId
import bcrypt



class JSONWEBTOKEN:

    ACCESS_TOKEN_SECRET_KEY =  os.getenv('JWT_ACCESS_TOKEN_SECRET_KEY') or "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7" 
    REFRESH_TOKEN_SECRET_KEY =  os.getenv('JWT_REFRESH_TOKEN_SECRET_KEY') or "09d25e004faa6ca2af6c818196b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7" 
    ALGORITHM =  os.getenv('JWT_ALGORITHM') or "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES') or 1
    REFRESH_TOKEN_EXPIRE_MINUTES = os.getenv('REFRESH_TOKEN_EXPIRE_MINUTES') or 30

    def create_access_token(self,data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.ACCESS_TOKEN_SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def create_refresh_token(self,data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=self.REFRESH_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.REFRESH_TOKEN_SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt
    
    def verify_access_token(self,access_token:str):
        try:
            payload = jwt.decode(access_token, self.ACCESS_TOKEN_SECRET_KEY, algorithms=[self.ALGORITHM])
            user_id = payload['id']
            return True,user_id
        except JWTError:
            return False,""
        
    def regenerate_access_token_from_refresh_token(self,refresh_token:str):
        try:
            payload = jwt.decode(refresh_token, self.REFRESH_TOKEN_SECRET_KEY, algorithms=[self.ALGORITHM])
            access_token_payload = {'email':payload['email'],'id':payload['id']}
            to_encode = access_token_payload.copy()
            expire = datetime.now(timezone.utc) + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
            to_encode.update({"exp": expire})
            encoded_jwt = jwt.encode(to_encode, self.ACCESS_TOKEN_SECRET_KEY, algorithm=self.ALGORITHM)
            return encoded_jwt,payload['id']
        except JWTError:
            raise HTTPException(status_code=401,detail="Unauthorized")
        




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

jwt_instance = JSONWEBTOKEN()




def get_user_detail_from_user_id(user_id:str) -> dict:
    '''
        This function will return the user details from user id
    '''

    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    db_user =  user_collection.find_one({'_id': ObjectId(user_id)})
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if db_user.get('disabled')==True:
        raise HTTPException(status_code=403, detail='User is disabled')

    serialized_user = serial(db_user)
    return serialized_user


def verify_auth(roles_allowed: list[str]):
    
    async def _verify_auth(request: Request, response: Response):
        authorization = request.cookies.get("access_token")
        access_token = authorization.split(" ")[1]
        refresh_token = request.cookies.get('refresh_token').split(" ")[1]
        status, user_id = jwt_instance.verify_access_token(access_token)
        if status == False:
            new_access_token, user_id = jwt_instance.regenerate_access_token_from_refresh_token(refresh_token)
            response.set_cookie(key='access_token', value=f'Bearer {new_access_token}', httponly=True)

        logged_in_user = get_user_detail_from_user_id(user_id=user_id)
        return logged_in_user
    
    return _verify_auth