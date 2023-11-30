from pydantic import BaseModel, StrictStr, Field


class LoginCredentials(BaseModel):
    login: StrictStr
    password: StrictStr
    rememberMe: bool
