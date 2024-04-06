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