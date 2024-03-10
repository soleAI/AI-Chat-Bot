from pydantic import BaseModel


class ResponseOnResumeUpload(BaseModel):
    message : str
    success : bool
    
