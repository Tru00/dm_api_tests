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
    login = 'test27'
    email = "testemail27@test.com"
    password = "123456"
    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    # activate user
    api.account.activate_registered_user(login=login)
    # login
    api.login.login_user(login=login, password=password)

# def check_input_json(json):
#     for key, value in json.items():
#         if key == 'login':
#             assert isinstance(value, str), f'Value in {key} should be str, but it is {type(value)}'
#         elif key == 'email':
#             assert isinstance(value, str), f'Value in {key} should be str, but it is {type(value)}'
#         elif key == 'password':
#             assert isinstance(value, str), f'Value in {key} should be str, but it is {type(value)}'
#
