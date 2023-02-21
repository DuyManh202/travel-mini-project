from playhouse.shortcuts import model_to_dict
from models.users import Users as UsersModel
from schema import user as user_schema
from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def login(payload_: user_schema.login):
    """Create a new user"""
    payload = payload_.dict()
    print(payload)
    # user = UsersModel.create(**payload)
    # return user.id
    query = UsersModel.select().where(
        UsersModel.email == payload["email"]).limit(1).dicts()
    users = list(query)
    if len(users) > 0: 
        user = users[0]
        if user["password"] == payload["password"]:
            return "okay"
        else:
            return "loss" 
    
    else:
        return "loss"         