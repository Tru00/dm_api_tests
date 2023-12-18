import time

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


def test_post_v1_account():
    api = Facade(host='http://localhost:5051')
    # register a new user
    login = 'test30'
    email = "testemail30@test.com"
    password = "123456"
    db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')
    db.delete_user_by_login(login=login) #delete user with this login from db
    dataset = db.get_user_by_login(login=login) #check if user is deleted
    for row in dataset:
        assert len(dataset) == 0

    api.mailhog.delete_all_messages() #delete email from mailhog

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'user {login} is not registered'
        assert row['Activated'] is False, f'user {login} is activated'

    # activate user
    api.account.activate_registered_user(login=login)
    time.sleep(2)
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'user {login} is not activated'

    # login
    api.login.login_user(login=login, password=password)


def test_activate_activated_account():
    api = Facade(host='http://localhost:5051')
    # register a new user
    login = 'test30'
    email = "testemail30@test.com"
    password = "123456"
    db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')
    db.delete_user_by_login(login=login)  # delete user with this login from db
    dataset = db.get_user_by_login(login=login)  # check if user is deleted
    for row in dataset:
        assert len(dataset) == 0

    api.mailhog.delete_all_messages()  # delete email from mailhog

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'user {login} is not registered'
        assert row['Activated'] is False, f'user {login} is activated'

    # activate user
    db.activate_user(login=login)
    api.account.activate_registered_user(login=login)

    time.sleep(2)
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'user {login} is not activated'

    # login
    api.login.login_user(login=login, password=password)