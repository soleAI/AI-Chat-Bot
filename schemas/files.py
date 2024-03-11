
import os
from fastapi import UploadFile,HTTPException
from models.file import File
from config.database import file_collection
import random
import string

def generate_random_string(length,extension = 'pdf'):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))+f'.{extension}'

class File_Upload():
    
    def __init__(self, file: UploadFile) -> None:
        self.root_path = os.getenv("FILE_UPLOAD_ROOT_PATH") or './uploads'
        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)
        self.file = file
        self.accepted_resume_format=['pdf','docx','doc','txt']
    
    async def upload_resume(self,uploader_id:str) -> str:
        try:
            file_name=self.file.filename
            extension=file_name.split(".")[-1]
            format_str=",".join(self.accepted_resume_format)
            
            if extension not in self.accepted_resume_format:
                raise HTTPException(status_code=400,detail= f"Please Upload {format_str} these formats only")
            contents = await self.file.read()
            random_string = generate_random_string(10)
            upload_path_dir = os.path.join(self.root_path, 'resume')
            if not os.path.exists(upload_path_dir):
                os.makedirs(upload_path_dir)

            upload_path = os.path.join(upload_path_dir, random_string)
            with open(upload_path, "wb") as f:
                f.write(contents)

            file_obj = File(original_file_name=self.file.filename,uploader_id=uploader_id,file_path=upload_path)
            inserted_file = file_collection.insert_one(dict(file_obj))
            inserted_id = inserted_file.inserted_id
            return str(inserted_id)
        
        except HTTPException as e:
           raise HTTPException(status_code=400,detail=e.detail)
        except Exception as e:
            raise HTTPException(status_code=400, detail="File Upload Error")