import peewee as p
# ket noi voi db
db = p.PostgresqlDatabase(
    'postgres',  # Required by Peewee.
    user='postgres',  # Will be passed directly to psycopg2.
    password='postgres',  # Ditto.
    host='db',
    port=5432)  # Ditto


class BaseModel(p.Model):
    class Meta:
        database = db
