import allure
import requests
from pydantic import BaseModel
from requests import Response
from ..models import *
from restclient.restclient import Restclient
from ..utilities import validate_request_json, validate_status_code


# from dm_api_account.models.user_envelope_model import UserEnvelopeModel
# from dm_api_account.models.user_details_envelope_model import UserDetailsEnvelopeModel




class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def get_v1_account(
            self,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserDetailsEnvelopeModel:

        '''
        Get current user
        :return:
        '''

        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )
        # validate_status_code(response, status_code)
        # if response.status_code == 200:
        #     return UserDetailsEnvelopeModel(**response.json())
        return response


    def post_v1_account(
            self,
            json: RegistrationModel,
            status_code: int = 201,
            **kwargs
    ) -> Response | UserEnvelopeModel:
        '''
        :param status_code:
        :param json registration_model
        Register new user
        :return:
        '''

        with allure.step('Register a new user'):
            response = self.client.post(
                path=f"/v1/account",
                json=validate_request_json(json),
                **kwargs
            )

        validate_status_code(response, status_code)
        # if response.status_code == 201:
        #     return UserEnvelopeModel(**response.json())
        return response

    def post_v1_account_password(
            self,
            json: ResetPassword,
            status_code: int = 201,
            **kwargs
    ) -> Response | UserEnvelopeModel:
        '''
        :param status_code:
        :param json reset_password
        Reset registered user password
        :return:
        '''

        response = self.client.post(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )

        validate_status_code(response, status_code)
        if response.status_code == 201:
            return UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_token(
            self,
            token: str,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelopeModel:
        '''
        Activate registered user
        :return:
        '''

        with allure.step('User activation'):
            response = self.client.put(
                path=f"/v1/account/{token}",
                **kwargs
            )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_email(
            self,
            json: ChangeEmail,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelopeModel:
        '''
        :param status_code:
        :param json change_email
        Change registered user email
        :return:
        '''

        response = self.client.put(
            path=f"/v1/account/email",
            json=validate_request_json(json),
            **kwargs)

        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_password(
            self,
            json: ChangePassword,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelopeModel:
        '''
        Change registered user password
        :return:
        '''

        response = self.client.put(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 201:
            return UserEnvelopeModel(**response.json())
        return response
