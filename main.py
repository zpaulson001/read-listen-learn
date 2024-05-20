from fastapi import Depends, FastAPI
from dotenv import load_dotenv
import schemas
import os

from requests import Session

from database import Base, SessionLocal, engine
from models import User

load_dotenv(".env")
database_url = os.getenv("DATABASE_URL")

# initialize db
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "look out world 👀"}


@app.post("/users", response_model=schemas.User)
async def create_users(db: Session = Depends(get_db)):
    user = User(email="me@me.com")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
