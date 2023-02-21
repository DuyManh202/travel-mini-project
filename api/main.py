from fastapi import FastAPI
from routers import *
from peewee import * 
from routers import users
from routers import login
app = FastAPI()
app.include_router(users.router, prefix='/users')
app.include_router(login.router, prefix='/login')
 