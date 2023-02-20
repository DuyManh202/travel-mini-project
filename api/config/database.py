from contextvars import ContextVar

import peewee

DB_NAME = 'postgres'
DATABASE = 'postgres'
USER = 'postgres'
PASSWORD = 'postgres'
POSTGRES_HOST = 'db'
POSTGRES_PORT = 5432
db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.PostgresqlExtDatabase(
    DB_NAME, user=USER, password=PASSWORD, host=POSTGRES_HOST, port=POSTGRES_PORT, check_same_thread=False
)

db._state = PeeweeConnectionState()