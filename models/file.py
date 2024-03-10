from pydantic import BaseModel,Field
from datetime import datetime


class File(BaseModel):
    original_file_name : str
    uploader_id : str
    upload_datetime:datetime = Field(default_factory=datetime.utcnow)
    file_path:str 

def serial_file(file) -> dict:
    return {
        'id':str(file['_id']),
        'original_file_name':file['filename'],
        'upload_datetime':file['upload_datetime'],
        'uploader_id':str(file['uploader_id']),
        'file_path':file['file_path']
    }

def list_serial_file(files)->list:
    return [serial_file[file] for file in files]