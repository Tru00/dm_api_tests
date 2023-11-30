from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field, condate


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


class ParseMode(Enum):
    COMMON = 'Common'
    INFO = 'Info'
    POST = 'Post'
    CHAT = 'Chat'


class Info(BaseModel):
    value: StrictStr
    parse_mode: Optional[List[ParseMode]] = Field(alias='ParseMode', default=None)


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSICPALE = 'ClassicPale'
    NIGHT = 'Night'


class Paging(BaseModel):
    postsPerPage: Optional[int] = Field(alias='postsPerPage', default=None)
    commentsPerPage: Optional[int] = Field(alias='commentsPerPage', default=None)
    topicsPerPage: Optional[int] = Field(alias='topicsPerPage', default=None)
    messagesPerPage: Optional[int] = Field(alias='messagesPerPage', default=None)
    entitiesPerPage: Optional[int] = Field(alias='entitiesPerPage', default=None)


class Settings(BaseModel):
    color_schema: Optional[List[ColorSchema]] = Field(alias='colorSchema', default=None)
    nanny_greetings_message: Optional[StrictStr] = Field(alias='nannyGreetingsMessage', default=None)
    paging: Paging


class UserDetails(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias='mediumPictureUrl', default=None)
    small_picture_url: Optional[StrictStr] = Field(alias='smallPictureUrl', default=None)
    status: Optional[StrictStr] = None
    rating: Rating
    online: Optional[condate] = None
    name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    registration: Optional[condate] = None
    icq: StrictStr
    skype: StrictStr
    original_picture_url: Optional[StrictStr] = Field(alias='originalPictureUrl', default=None)
    info: Info
    settings: Settings


class UserDetailsEnvelopeModel(BaseModel):
    resource: UserDetails = None
    metadata: Optional[StrictStr] = None
