import peewee as p
# ket noi voi db
from config.database import db

class BaseModel(p.Model):
    class Meta:
        database = db
