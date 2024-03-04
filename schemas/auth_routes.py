from pydantic import BaseModel,field_validator
import re
from schemas.errors import FieldValidateError



class UserSignUp(BaseModel):
    email : str
    name : str 
    mobile_num:str
    password:str
    confirm_password:str

    @field_validator('email')
    def validate_email(cls,value):
        '''Validating the email'''
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(regex, value):
            raise FieldValidateError("Please Enter valid Email")
        return value
    

# similarily all the schemas used in auth routes will be here