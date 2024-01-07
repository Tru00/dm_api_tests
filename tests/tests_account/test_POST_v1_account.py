import time

import allure
import pytest
from collections import namedtuple
from hamcrest import assert_that, has_entries
from string import ascii_letters, printable, digits
import random
from data.post_v1_account import PostV1AccountData as user_data


def random_string():
    symbols = ascii_letters + digits
    string = ''
    for _ in range(10):
        string += random.choice(symbols)
    return string


@allure.suite("Check method POST v1/account")
@allure.sub_suite("Positive tests")
class TestsPostV1Account:
    @allure.step("setup test user")
    @pytest.fixture
    def prepare_user(self, dm_api_facade, dm_db):
        user = namedtuple('User', 'login, email, password')
        User = user(login=user_data.login, email=user_data.email, password=user_data.password)
        dm_db.delete_user_by_login(login=User.login)  # delete user with this login from db
        dataset = dm_db.get_user_by_login(login=User.login)  # check if user is deleted
        assert len(dataset) == 0

        dm_api_facade.mailhog.delete_all_messages()  # delete email from mailhog
        return User

    @allure.title("test user registration and activation")
    def test_register_and_activate_user(self, dm_api_facade, dm_db, prepare_user, assertions):
        """
        test user creation and user activation in database
        """
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

        dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password
        )

        assertions.check_user_was_created(login=login)

        # activate user
        dm_api_facade.account.activate_registered_user(login=login)
        assertions.check_user_was_activated(login=login)
        # login
        dm_api_facade.login.login_user(login=login, password=password)

    # @pytest.mark.parametrize('login, email, password', [
    #     ('test30', 'testemail30@test.com', '123456'),
    #     ('test', 'testemail@test.com', '123456'),
    #     ('30303030', '30303030@test.com', '30303030'),
    # ])

    @pytest.mark.parametrize('login', [random_string() for _ in range(3)])
    @pytest.mark.parametrize('email', [random_string() + '@' + random_string() + '.com' for _ in range(3)])
    @pytest.mark.parametrize('password', [random_string() for _ in range(3)])
    def test_create_and_activate_user_with_random_params(self, dm_api_facade, dm_db, login, email, password,
                                                         assertions):
        dm_db.delete_user_by_login(login=login)  # delete user with this login from db
        dm_api_facade.mailhog.delete_all_messages()  # delete email from mailhog
        dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password
        )
        assertions.check_user_was_created(login=login)
        # activate user
        dm_api_facade.account.activate_registered_user(login=login)
        assertions.check_user_was_activated(login=login)

        # login
        dm_api_facade.login.login_user(login=login, password=password)

# def test_activate_activated_account():
#     api = Facade(host='http://localhost:5051')
#     # register a new user
#     login = 'test30'
#     email = "testemail30@test.com"
#     password = "123456"
#     db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')
#     db.delete_user_by_login(login=login)  # delete user with this login from db
#     dataset = db.get_user_by_login(login=login)  # check if user is deleted
#     for row in dataset:
#         assert len(dataset) == 0
#
#     api.mailhog.delete_all_messages()  # delete email from mailhog
#
#     response = api.account.register_new_user(
#         login=login,
#         email=email,
#         password=password
#     )
#     dataset = db.get_user_by_login(login=login)
#     for row in dataset:
#         assert row['Login'] == login, f'user {login} is not registered'
#         assert row['Activated'] is False, f'user {login} is activated'
#
#     # activate user
#     db.activate_user(login=login)
#     api.account.activate_registered_user(login=login)
#
#     time.sleep(2)
#     dataset = db.get_user_by_login(login=login)
#     for row in dataset:
#         assert row['Activated'] is True, f'user {login} is not activated'
#
#     # login
#     api.login.login_user(login=login, password=password)
