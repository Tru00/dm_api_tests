import pytest
from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
from generic.helpers.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import RegistrationModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)  # make a log


@pytest.fixture
def mailhog():
    return MailhogApi(host='http://localhost:5025')


@pytest.fixture
def dm_api_facade(mailhog):
    return Facade(host='http://localhost:5051', mailhog=mailhog)


@pytest.fixture
def dm_db():
    db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')
    return db