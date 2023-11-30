from pydantic import BaseModel, StrictStr, Field


class ResetPassword(BaseModel):
    login: StrictStr
    email: StrictStr
