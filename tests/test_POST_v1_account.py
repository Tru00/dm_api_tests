import requests
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import RegistrationModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host='http://localhost:5025/')
    api = DmApiAccount(host='http://localhost:5051')
    # json = RegistrationModel(
    #     login="test10",
    #     email="testemail10@test.com",
    #     password="123456"
    # )
    #
    # response = api.account.post_v1_account(
    #     json=json
    # )
    # assert response.status_code == 201, f'status code should be 201, but it is {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)


# def check_input_json(json):
#     for key, value in json.items():
#         if key == 'login':
#             assert isinstance(value, str), f'Value in {key} should be str, but it is {type(value)}'
#         elif key == 'email':
#             assert isinstance(value, str), f'Value in {key} should be str, but it is {type(value)}'
#         elif key == 'password':
#             assert isinstance(value, str), f'Value in {key} should be str, but it is {type(value)}'
#
