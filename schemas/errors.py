from fastapi import HTTPException

class FieldValidateError(HTTPException):
    '''Custom Error While Validating the Field of model'''
    def __init__(self, message: str):
        self.status_code = 403
        self.message = message
        super().__init__(status_code=self.status_code,detail=message)

class FieldNotPresentError(HTTPException):
    '''Error handler when required field is not present'''

    def __init__(self,status_code:int=401,message:str='Required feild not present'):
        self.status_code=status_code
        self.message = message
        super().__init__(status_code=status_code,detail=message)

class InternalServerError(HTTPException):
    '''Error Handler for Internal Server Error'''
    def __init__(self, status_code: int=500, message: str='Internal Server Error'):
        self.status_code = status_code
        self.message = message
        super().__init__(status_code=status_code,detail=message)

class NotFoundError(HTTPException):
    '''Error will be thrown on not found'''
    def __init__(self, status_code: int=404, message: str='Not Found'):
        self.status_code = status_code
        self.message = message
        super().__init__(status_code=status_code,detail=message)

