from fastapi import FastAPI
from app.api import chat

app = FastAPI(title="AIVA Backend")
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "AIVA running 🚀"}