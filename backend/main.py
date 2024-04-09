from fastapi import FastAPI
from pymongo import MongoClient;
from dotenv import load_dotenv
import os

load_dotenv()

client=MongoClient(os.getenv("MONGO_DB"))
print(client.list_database_names())

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello Wrld"}

@app.get("/db")
async def db():
    database_name=client.list_database_names()
    db=client['admin']
    x=db.list_collection_names()
    return {"Db name and List in DB": database_name}