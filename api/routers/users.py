from playhouse.shortcuts import model_to_dict
from models.users import Users as UsersModel
from schema import user as user_schema
from fastapi import APIRouter

router = APIRouter()

@router.get("/api/users")
def get_all_users():
    """Get all users"""
    
    users = UsersModel.select().order_by(UsersModel.id.desc(),)
    users = [model_to_dict(user) for user in users]
    return users


@router.post("/api/users")
def create_user(payload_: user_schema.UserCreate):
    """Create a new user"""
    payload = payload_.dict()
    user = UsersModel.create(**payload)
    return user.id


@router.patch("/api/users/{id}")
def edit_user(id: int, payload_: user_schema.UserUpdate):
    """Update user info"""
    payload = payload_.dict()
    user = (
        UsersModel.update(
            ib =payload["id"],
            email=payload["email"],
            password=payload["password"],
            name=payload["name"],
            phone_number=payload["phone_number"],
            address=payload["address"],
            is_admin=payload["is_admin"],
        )
        
        .where(UsersModel.id == id)
        .execute()
    )
    # number of changed rows
    return user

@router.delete("/api/users/{id}")
def user_employee(id: int):
    """Delete user"""
    user = UsersModel.get_by_id(id)
    user.delete_instance()
                                        
                                        
                                        
                                        
                                        
                                        
                                        