import requests
from requests import Response
from ..models.registration_model import RegistrationModel
from ..models.reset_password import ResetPassword
from ..models.change_email import ChangeEmail
from ..models.change_password import ChangePassword
from requests import session
from restclient.restclient import Restclient
from dm_api_account.models.user_envelope_model import UserEnvelopeModel
from dm_api_account.models.user_details_envelope_model import UserDetailsEnvelopeModel


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

        #self.session.headers.update(headers) if headers else None #The same as previos 2 lines

    def get_v1_account(self, **kwargs) -> Response:
        '''
        Get current user
        :return:
        '''

        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )

        UserDetailsEnvelopeModel(**response.json())
        return response

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        '''
        :param json registration_model
        Register new user
        :return:
        '''

        response = self.client.post(
            path=f"/v1/account",
            json=json.model_dump(by_alias=True, exclude_none=True), #exclude_none=True - turn off not-required fields
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def post_v1_account_password(self, json: ResetPassword, **kwargs) -> Response:
        '''
        :param json reset_password
        Reset registered user password
        :return:
        '''

        response = self.client.post(
            path=f"/v1/account/password",
            json=json,
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        '''
        Activate registered user
        :return:
        '''

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmail, **kwargs) -> Response:
        '''
        :param json change_email
        Change registered user email
        :return:
        '''

        response = self.client.put(
            path=f"/v1/account/email",
            json=json,
            **kwargs)
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePassword, **kwargs) -> Response:
        '''
        Change registered user password
        :return:
        '''


        response = self.client.put(
            path=f"/v1/account/password",
            json=json,
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response
