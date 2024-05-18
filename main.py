from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv(".env")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "look out world 👀"}
