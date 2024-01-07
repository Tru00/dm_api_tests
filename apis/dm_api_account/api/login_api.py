from requests import Response

from common_libs.restclient.restclient import Restclient
from ..utilities import validate_request_json
from apis.dm_api_account.models import *


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentials, **kwargs) -> Response:
        '''
        :param json: login_credentials
        Authenticate via credentials
        :return:
        '''

        response = self.client.post(
            path=f"/v1/account/login",
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

        response = self.client.delete(
            path=f"/v1/account/login",
            **kwargs
        )

        return response

    def delete_v1_account_login_all(self, **kwargs):
        '''
        Logout from every device
        :return:
        '''

        response = self.client.delete(
            path=f"/v1/account/login/all",
            **kwargs
        )

        return response
