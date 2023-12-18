import json
import time

import structlog
from requests import session, Response
from restclient.restclient import Restclient

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)  # make a log


def decorator(fn):
    def wrapper(*arg, **kwargs):
        for i in range(5):
            response = fn(*arg, **kwargs)
            emails = response.json()['items']
            if len(emails) < 1:
                print(f'attempt {i}')
                continue
            else:
                return response

    return wrapper


class MailhogApi:
    def __init__(self, host='http://localhost:5025'):
        self.host = host
        self.client = Restclient(host=host)

    @decorator
    def get_api_v2_messages(self, limit: int = 50) -> Response:
        """
        Get messages by limit
        :param limit:
        :return:
        """
        response = self.client.get(
            path=f"/api/v2/messages",
            params={
                'limit': limit
            }
        )

        return response

    def get_token_from_last_email(self) -> str:
        """
        Get user activation token from the last email
        :return:
        """
        emails = self.get_api_v2_messages(limit=1).json()
        token_url = json.loads(emails['items'][0]['Content']['Body'])['ConfirmationLinkUrl']
        token = token_url.split('/')[-1]
        return token

    def get_token_by_login(self, login: str, attempt=50):
        if attempt == 0:
            raise AssertionError(f'There is no email with login {login}')
        time.sleep(2)
        emails = self.get_api_v2_messages(limit=100).json()['items']
        for email in emails:
            user_data = json.loads(email['Content']['Body'])
            if login == user_data.get('Login'):
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
                print(f'token = {token}')
                return token
        time.sleep(2)
        return self.get_token_by_login(login=login, attempt=attempt - 1)

    def delete_all_messages(self):
        response = self.client.delete(path='/api/v1/messages')
        return response



if __name__ == '__main__':
    MailhogApi().get_token_by_login('login30')
