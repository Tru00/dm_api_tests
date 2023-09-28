import requests
from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "<string>",
        "email": "<string>",
        "password": "<string>"
    }
    response = api.account.post_v1_account(
        json=json
    )
    print(response)
