from fastapi import FastAPI
from routers import *
from peewee import * 
from routers import users
from routers import admin 

app = FastAPI()
app.include_router(users.router)
app.include_router(admin.router)

@app.get("/")
def root_access():
    return {"message": "Hello World"}

@app.get("/abc")
def test_api():
    return {"message": "Hello World 2"}

@app.post("/test")
def test_post():
    return{"aadas"}
 
 