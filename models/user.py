from pydantic import BaseModel,Field


class User(BaseModel):
    email : str
    name : str 
    mobile_num: str
    password:str
    onobarding_step:int = Field(default=1)
    onboarded:bool = Field(default=False)
    disabled:bool = Field(default=False)

def serial(user) -> dict:
    return {
        "id":str(user['_id']),
        "name":user['name'],
        'email':user['email'],
        'mobile_num':user['mobile_num'],
        'onboarding_step':user['onobarding_step'],
        'onboarded':user['onboarded']
    }

def list_serial(users)->list:
    return [serial[user] for user in users]