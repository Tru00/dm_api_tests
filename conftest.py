import pytest
import structlog

from generic.assertions.post_v1_account import AssertionsPostV1Account
from generic.helpers.dm_db import DmDatabase
from generic.helpers.mailhog import MailhogApi
from services.dm_api_account import Facade
from vyper import v
from pathlib import Path

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)  # make a log


@pytest.fixture
def mailhog():
    return MailhogApi(host=v.get('service.mailhog'))


@pytest.fixture
def dm_api_facade(mailhog):
    return Facade(
        host=v.get('service.dm_api_account'),
        mailhog=mailhog
    )


options = (
    'service.dm_api_account',
    'service.mailhog',
    'database.dm3_5.host'
)

connect = None
@pytest.fixture
def dm_db():
    global connect
    if connect is None:      # check if we have connection we do not create a new one
        connect = DmDatabase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        host=v.get('database.dm3_5.host'),
        database=v.get('database.dm3_5.database'),
    )
    yield connect
    connect.db.db.close()


@pytest.fixture
def assertions(dm_db):
    return AssertionsPostV1Account(dm_db)


@pytest.fixture(autouse=True)
def set_config(request):
    config = Path(__file__).parent.joinpath('config')  # go from the current file to config file
    config_name = request.config.getoption('--env')  # get the name of our config
    v.set_config_name(config_name)  # set config name
    v.add_config_path(config)  # path to our config
    v.read_in_config()
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))  # read all options


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stg')
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)
