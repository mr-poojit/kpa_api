from fastapi import FastAPI
from app.routers import user, document
from app.database import Base, engine
from app.models import User, Document

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(document.router)