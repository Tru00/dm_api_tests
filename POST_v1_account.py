import requests
import json


def post_v1_account():
    '''
    Register new user
    :return:
    '''
    url = "http://localhost:5051/v1/account"

    payload = {
        "login": "<string>",
        "email": "<string>",
        "password": "<string>"
    }
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload
    )

    return response

