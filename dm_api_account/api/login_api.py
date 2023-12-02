import requests
from requests import Response
from ..models import *
#from ..models.login_credentials import LoginCredentials
from requests import session
from dm_api_account.models.user_envelope_model import UserEnvelopeModel
from ..utilities import validate_request_json


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentials, **kwargs) -> Response:
        '''
        :param json: login_credentials
        Authenticate via credentials
        :return:
        '''

        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=validate_request_json(json),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def delete_v1_account_login(self, **kwargs):
        '''
        Logout as current user
        :return:
        '''

        response = self.session.delete(
            url=f"{self.host}/v1/account/login",
            **kwargs
        )

        return response

    def delete_v1_account_login_all(self, **kwargs):
        '''
        Logout from every device
        :return:
        '''

        response = self.session.delete(
            url=f"{self.host}/v1/account/login/all",
            **kwargs
        )

        return response
