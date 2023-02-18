from playhouse.shortcuts import model_to_dict
from peewee import fn
from models.users import Users
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

@router.get("/api/users")
def get_all_users():
    """Get all users"""
    
    users = Users.select().order_by(Users.id.desc(),)
    users = [model_to_dict(user) for user in users]
    return users


@router.post("/api/users")
def create_user(payload_: Users):
    """Create a new user"""
    print("ada")
    payload = payload_.dict()
    user = Users.create(**payload)
    return user.id


@router.patch("/api/users/{id}", response_model=int)
def edit_user(id: int, payload_: Users):
    """Update user info"""
    payload = payload_.dict()
    user = (
        Users.update(
            ib =payload["id"],
            email=payload["email"],
            password=payload["password"],
            name=payload["name"],
            phone_number=payload["phone_number"],
            address=payload["address"],
            is_admin=payload["is_admin"],
        )
        
        .where(Users.id == id)
        .execute()
    )
    # number of changed rows
    return user


@router.delete("/api/users/{id}")
def user_employee(id: int):
    """Delete user"""
    user = Users.get_by_id(id)
    user.delete_instance()
                                        
                                        
                                        
                                        
                                        
                                        
                                        