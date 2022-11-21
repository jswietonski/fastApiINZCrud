from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import api


app = FastAPI()

app.include_router(api.router)



@app.get('/')
def root_api():
    return {"message": "Pierwszy mikroserwis do wystawienia w kontenerze dockera"}


origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)