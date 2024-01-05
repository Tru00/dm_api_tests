import allure
from hamcrest import assert_that, has_entries
from generic.helpers.dm_db import DmDatabase


class AssertionsPostV1Account:

    def __init__(self, db: DmDatabase):
        self.db = db

    def check_user_was_created(self, login):
        with allure.step('Check if user was created'):
            dataset = self.db.get_user_by_login(login=login)
            for row in dataset:
                assert_that(row, has_entries(
                    {
                        'Login': login,
                        'Activated': False
                    }
                ))

    def check_user_was_activated(self, login):
        with allure.step('Check if user was activated'):
            dataset = self.db.get_user_by_login(login=login)
            for row in dataset:
                assert row['Activated'] is True, f'user {login} is not activated'