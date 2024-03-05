from pydantic import BaseModel,Field
from datetime import datetime

class User(BaseModel):
    email : str
    name : str 
    mobile_num: str
    password:str
    onobarding_step:int = Field(default=1)
    onboarded:bool = Field(default=False)
    disabled:bool = Field(default=False)
    created_datetime: datetime 
    updated_datetime : datetime = Field(default_factory=datetime.utcnow)

def serial(user) -> dict:
    return {
        "id":str(user['_id']),
        "name":user['name'],
        'email':user['email'],
        'mobile_num':user['mobile_num'],
        'onboarding_step':user['onobarding_step'],
        'onboarded':user['onboarded'],
        'created_datetime':user['created_datetime'],
        'updated_datetime':user['updated_datetime']
    }

def list_serial(users)->list:
    return [serial[user] for user in users]