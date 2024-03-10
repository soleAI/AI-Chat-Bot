from fastapi import APIRouter,HTTPException,Response,Depends
from schemas.auth_routes import UserSignUp,UserLogin,ResponseWithToken
from models.user import (User,serial)
from datetime import datetime
from config.database import user_collection
from middlewares.auth import (jwt_instance,verify_auth,Bcrypts)
from models.user import UserRole

router = APIRouter()

def convert_enum_to_str(user):
    user_dict = user.dict()
    user_dict["role"] = user_dict["role"].value
    return user_dict


@router.post("/sign-up")
async def sign_up(user:UserSignUp,response:Response):
    '''
        This function is responsible for signing up a user with email and password
    '''
    hashed_password : str = Bcrypts.get_hash(user.password)
    new_user:User = User(name=user.name, email=user.email, password=hashed_password,mobile_num=user.mobile_num,created_datetime=datetime.utcnow(),updated_datetime=datetime.utcnow())
    existing_user = user_collection.find_one({'$or':[{'email':new_user.email},{'mobile_num':new_user.mobile_num}]})

    if existing_user:
        raise HTTPException(status_code=403,detail='User Already Exist with same mobile/email')
    new_user = convert_enum_to_str(new_user)
    insert_result = user_collection.insert_one(new_user)
    inserted_id = insert_result.inserted_id
    inserted_user = user_collection.find_one({'_id': inserted_id})
    inserted_user =  serial(inserted_user)

    access_token = jwt_instance.create_access_token(data={'email':inserted_user['email'],'id':inserted_user['id']})
    refresh_token = jwt_instance.create_refresh_token(data={'email':inserted_user['email'],'id':inserted_user['id']})

    response.set_cookie(key='access_token',value=f'Bearer {access_token}',httponly=True)
    response.set_cookie(key='refresh_token',value=f'Bearer {refresh_token}',httponly=True)
    
    return ResponseWithToken(user=inserted_user,access_token=access_token, token_type="bearer")


@router.post("/sign-in")
async def sign_in(user:UserLogin,response:Response):
    '''
        This function is responsible for signing in a user with email and password
    '''

    db_user = user_collection.find_one({'email':user.email})
    if not db_user:
        raise HTTPException(status_code=404,detail='Enter valid credentials')
    if db_user['disabled']==True:
        raise HTTPException(status_code=403,detail='User is disabled')
    
    hashed_password = db_user['password']
    db_user = serial(db_user)
    if Bcrypts.compare(user.password,hashed_password)==False:
        raise HTTPException(status_code=404,detail='Enter valid credentials')
    
    access_token = jwt_instance.create_access_token(data={'email':db_user['email'],'id':db_user['id']})
    refresh_token =jwt_instance.create_refresh_token(data={'email':db_user['email'],'id':db_user['id']})
    
    response.set_cookie(key='access_token',value=f'Bearer {access_token}',httponly=True)
    response.set_cookie(key='refresh_token',value=f'Bearer {refresh_token}',httponly=True)
    return ResponseWithToken(user=db_user,access_token=access_token, token_type="bearer")



@router.get("/get_me")
async def get_me(logged_in_user: dict = Depends(verify_auth(roles_allowed=[UserRole.USER]))):
    '''
        This function will return the current logged in user
    '''
    user = logged_in_user
    return user
    



  