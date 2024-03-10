from fastapi import APIRouter,Depends,UploadFile
from middlewares.auth import (verify_auth)
from models.user import UserRole
from schemas.files import File_Upload
from schemas.onboarding_routes import ResponseOnResumeUpload

router = APIRouter()

@router.post("/resume_upload")
async def resume_upload(file:UploadFile,logged_in_user:dict = Depends(verify_auth(roles_allowed=[UserRole.USER,UserRole.ADMIN]))):
    '''
        This function will upload resume file
    '''
    
    new_file = File_Upload(file=file)
    file_id : str = await new_file.upload_resume(logged_in_user['id'])
    
    return ResponseOnResumeUpload(message="Resume Uploaded Successfully",success=True)

