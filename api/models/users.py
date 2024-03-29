from . import PeeWeeBaseModel
from models.base_model import BaseModel
import peewee as p


class Users(BaseModel):
    email = p.TextField()
    password = p.TextField()
    name = p.TextField()
    phone_number = p.TextField()
    address = p.TextField()
    is_admin = p.BooleanField()

    class Meta:
        db_table = 'users'

    @classmethod
    # def get_list(cls):
    #     query = cls.select().order_by(score)
    #     return list(query)
    def get_user(cls,data):
        query = Users.select().where(
            Users.email == data['email'] and Users.password == data['password'])
        query = list(query)
        if len(query):
            return {"code": 200, "data": query}
        else:
            return {"code": 400, 'data': query}
