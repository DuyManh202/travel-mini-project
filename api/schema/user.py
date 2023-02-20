from schema.base import BaseModel

class UsersBase(BaseModel):
    email: str = None
    password: str
    name: str
    phone_number: str = None
    address: str = None
    is_admin: bool = False


class Users(UsersBase):
    id: int


class UserCreate(UsersBase):
    pass


class UserUpdate(UsersBase):
    id: int