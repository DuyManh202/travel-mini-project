from . import PeeWeeBaseModel
from base_model import BaseModel
import peewee as p

class Travels(BaseModel):
    id = p.PrimaryKeyField()
    title = p.TextField()
    img = p.TextField()
    content = p.TextField()
    day = p.DateTimeField()
    time = p.TimestampField()
