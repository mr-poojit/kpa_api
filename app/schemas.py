from pydantic import BaseModel
from fastapi import Form

class UserCreateForm:
    def __init__(
        self,
        phone_number: str = Form(...),
        password: str = Form(...)
    ):
        self.phone_number = phone_number
        self.password = password

class DocumentResponse(BaseModel):
    filename: str
    path: str
