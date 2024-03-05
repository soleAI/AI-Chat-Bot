from pydantic import BaseModel,field_validator,EmailStr
import re
from schemas.errors import FieldValidateError,FieldNotPresentError
from email_validator import validate_email as validate_email_address


mobile_regex = r'^\d{10}$'
name_regex = r'^[A-Za-z\s]+$'  # Allows only alphabets and spaces

class UserSignUp(BaseModel):
    email : str
    name : str 
    mobile_num:str
    password:str
    confirm_password:str

    def __init__(self, **data):
        super().__init__(**data)
        fields_not_present:list = []
        for field_name, field in self.model_fields.items():
            if field.is_required and field_name not in data:
                fields_not_present.append(field_name)
        if len(fields_not_present)!=0:
            raise FieldNotPresentError(message=f"Field{'s' if len(fields_not_present)>1 else ''} : '{ ', '.join(fields_not_present)}' not present.")

    @field_validator('email')
    def validate_email(cls, value):
        '''Validating the email'''
        try:
            validate_email_address(value)
        except Exception:
            raise FieldValidateError("Please Enter a valid Email")
        return value
    
    @field_validator('mobile_num')
    def validate_mobile(cls,value):
        '''Validating the mobile nuumber'''

        if not re.match(mobile_regex,value):
            raise FieldValidateError("Enter a valid Mobile Number")
        return value

    @field_validator('name')
    def validate_mobile(cls,value):
        '''Validating the Name'''

        if not re.match(name_regex,value):
            raise FieldValidateError("Enter a valid name with only alphabetical character")
        return value
    
    @field_validator('password')
    def validate_password(cls, value):
        '''Validating the password'''

        if len(value) < 8:
            raise FieldValidateError("Password must be at least 8 characters long")
        if not re.search(r'[A-Z]', value):
            raise FieldValidateError("Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', value):
            raise FieldValidateError("Password must contain at least one lowercase letter")
        if not re.search(r'\d', value):
            raise FieldValidateError("Password must contain at least one digit")
        return value
    

    @field_validator('confirm_password')
    def validate_confirm_password(cls, value, values):
        '''Validating the confirm password'''
        if 'password' in values.data and value != values.data['password']:
            raise FieldValidateError("Passwords do not match")
        return value
    

class UserLogin(BaseModel):
    email:EmailStr
    password:str

    def __init__(self, **data):
        super().__init__(**data)
        fields_not_present:list = []
        for field_name, field in self.model_fields.items():
            if field.is_required and field_name not in data:
                fields_not_present.append(field_name)
        if len(fields_not_present)!=0:
            raise FieldNotPresentError(message=f"Field{'s' if len(fields_not_present)>1 else ''} : '{ ', '.join(fields_not_present)}' not present.")

    @field_validator('email')
    def validate_email(cls, value):
        '''Validating the email'''
        try:
            validate_email_address(value)
        except Exception:
            raise FieldValidateError("Please Enter a valid Email")
        return value
    



class ResponseWithToken(BaseModel):
    user:dict
    access_token: str
    token_type: str
    
