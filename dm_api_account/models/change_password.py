from pydantic import BaseModel, StrictStr, Field


class ChangePassword(BaseModel):
    login: StrictStr
    token: StrictStr
    oldPassword: StrictStr
    newPassword: StrictStr
