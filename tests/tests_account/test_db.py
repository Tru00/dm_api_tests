import structlog
from generic.helpers.dm_db import DmDatabase
from generic.helpers.orm_db import OrmDatabase
from generic.helpers.orm_models2 import Users

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)  # make a log


def test_orm():
    user = 'postgres'
    password = 'admin'
    host = 'localhost'
    database = 'dm3.5'
    orm = OrmDatabase(user=user, password=password, host=host, database=database)

    #dataset = orm.get_all_users()
    dataset = orm.get_user_by_login('test30')
    for row in dataset:
        print(row.Name)
        print(row.Login)
        print(row.Email)

    orm.db.close_connection()


def test_db():
    db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')
    db.get_all_users()
