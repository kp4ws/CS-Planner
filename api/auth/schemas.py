from pydantic import BaseModel

class LoginRequest(BaseModel):
    username : str
    password : str
    #TODO email

class RegisterRequest(BaseModel):
    username: str
    password: str
    #TODO email