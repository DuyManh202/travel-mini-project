from . import PeeWeeBaseModel
from base_model import BaseModel
import peewee as p

class Comments(BaseModel):
    id = p.PrimaryKeyField()
    user = p.TextField()
    post = p.IntegerField()
    comments = p.TextField()