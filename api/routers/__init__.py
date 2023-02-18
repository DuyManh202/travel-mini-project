from fastapi import APIRouter

router = APIRouter()


from .users import *
from .admin import *
