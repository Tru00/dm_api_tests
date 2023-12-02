import structlog
from dm_api_account.models.user_envelope_model import Roles
from services.dm_api_account import DmApiAccount
import json
from hamcrest import assert_that, has_properties # validate incoming json values

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = DmApiAccount(host='http://localhost:5051')
    response = api.account.put_v1_account_token(token='791eb272-67fb-48cd-b2c5-a9ae7da77fc1', status_code=200)
    assert_that(response.resource, has_properties(
        {
            'login': 'test11',
            'roles': [Roles.GUEST, Roles.PLAYER]

        }
    ))





    # expected_json = {'resource': {
    #     'login': 'test17',
    #     'roles': [
    #         'Guest',
    #         'Player'
    #     ],
    #     'rating': {
    #         'enabled': True,
    #         'quality': 0,
    #         'quantity': 0
    #     }
    # }
    # }
    # actual_json = (json.loads(response.json(by_alias=True, exclude_none=True)))
    # assert actual_json == expected_json
