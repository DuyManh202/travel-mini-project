from . import PeeWeeBaseModel
import peewee as p
from base_model import BaseModel


class Blogs(BaseModel):
    id = p.PrimaryKeyField()
    title = p.TextField()
    img = p.TextField()
    content = p.TextField()
    type = p.TextField
    
    class Meta:
        db_table = 'blogs'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)
