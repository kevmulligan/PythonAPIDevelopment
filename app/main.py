from ast import Delete
from typing import Optional, List
from typing_extensions import deprecated
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from time import sleep
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, SessionLocal, get_db
from .routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='root', 
                                password='root', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("DB connection successful")
        break
    except Exception as error:
        print("Connecting to DB failed")
        print("Error: ", error)
        sleep(5)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "fav foods", "content" : "I like pizza", "id": 2}]

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "welcome to my api"}



