from fastapi import APIRouter
from app.services.llm.provider import generate_response

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.get("/")
def test_chat():
    return {"response": generate_response("Explain RAG in simple terms")}