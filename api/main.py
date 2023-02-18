from fastapi import FastAPI
from routers import *
from peewee import * 
from routers import users
from routers import admin 

app = FastAPI()
app.include_router(users.router, prefix='/users')
# app.include_router(admin.router, prefix='/admin')
 