from pydantic import BaseModel, StrictStr, Field


class ChangeEmail(BaseModel):
    login: StrictStr
    password: StrictStr
    email: StrictStr
