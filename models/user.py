from pydantic import BaseModel,Field
from typing import Optional

class User(BaseModel):
    email : str
    name : str 
    mobile_num: Optional[str]
    password:str
    onobarding_step:int = Field(default=1)
    verified:bool = Field(default=False)

def serial(user) -> dict:
    return {
        "id":str(user['_id']),
        "name":user['name'],
        'email':user['email'],
        'password':user['password'],
        'onboarding_step':user['onobarding_step'],
        'verified':user['verified']
    }

def list_serial(users)->list:
    return [serial[user] for user in users]