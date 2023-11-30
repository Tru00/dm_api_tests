from pydantic import BaseModel, StrictStr, Field
from enum import Enum
from typing import List


class RegistrationModel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr

# registration_model = {
#     "login": "string",
#     "Email": "<string>",
#     "password": "<string>",
#     "roles": ["manager", "user"]
# }

# class Roles(Enum):
#     MANAGER = 'manager'
#     USER = 'user'
#
# class RegistrationModel(BaseModel):
#     roles: List[Roles]
#     login: StrictStr = Field(default='test_value')
#     email: StrictStr = Field(alias='Email', title='email')
#     password: StrictStr = Field(min_length=5)
#
# print(RegistrationModel(**registration_model).model_dump_json())
