import requests
from requests import Response
from ..models.registration_model import registration_model
from ..models.reset_password import reset_password
from ..models.change_email import change_email
from ..models.change_password import change_password
from requests import session


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)

        #self.session.headers.update(headers) if headers else None #The same as previos 2 lines

    def get_v1_account(self, **kwargs):
        '''
        Get current user
        :return:
        '''

        response = self.session.get(
            url=f"{self.host}/v1/account",
            **kwargs
        )

        return response

    def post_v1_account(self, json: registration_model, **kwargs) -> Response:
        '''
        :param json registration_model
        Register new user
        :return:
        '''

        response = self.session.post(
            url=f"{self.host}/v1/account",
            json=json,
            **kwargs
        )

        return response

    def post_v1_account_password(self, json: reset_password, **kwargs) -> Response:
        '''
        :param json reset_password
        Reset registered user password
        :return:
        '''

        response = self.session.post(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )

        return response

    def put_v1_account_token(self, **kwargs):
        '''
        Activate registered user
        :return:
        '''

        response = self.session.put(
            url=f"{self.host}/v1/account/<uuid>",
            **kwargs
        )

        return response

    def put_v1_account_email(self, json: change_email, **kwargs) -> Response:
        '''
        :param json change_email
        Change registered user email
        :return:
        '''

        response = self.session.put(
            url=f"{self.host}/v1/account/email",
            json=json,
            **kwargs)

        return response

    def put_v1_account_password(self, json:change_password, **kwargs) -> Response:
        '''
        Change registered user password
        :return:
        '''


        response = self.session.put(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )

        return response