from pydantic import BaseModel, StrictStr, Field
from typing import Optional


class LoginCredentials(BaseModel):
    login: StrictStr
    password: StrictStr
    remember_me: Optional[bool] = Field(None, alias='rememberMe')
