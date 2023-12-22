from typing import List

from sqlalchemy import select

from orm_client.orm_client import OrmClient
from generic.helpers.orm_models2 import Users



class OrmDatabase:

    def __init__(self, user, password, host, database):
        self.db = OrmClient(user, password, host, database)

    def get_all_users(self):
        query = select([Users])
        dataset = self.db.send_query(query)
        return dataset

    def get_user_by_login(self, login) -> List[Users]:
        query = select([Users]).where(
            Users.Login == login
        )
        dataset = self.db.send_query(query)
        return dataset




