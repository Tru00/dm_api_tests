import datetime
from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field, StrictBool, condate, validator


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias='mediumPictureUrl', default=None)
    small_picture_url: Optional[StrictStr] = Field(alias='smallPictureUrl', default=None)
    status: Optional[StrictStr] = None
    rating: Rating
    online: Optional[datetime] = Field(None)
    name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    registration: Optional[datetime] = Field(None)


class UserEnvelopeModel(BaseModel):
    resource: Optional[User] = None
    metadata: Optional[StrictStr] = None
