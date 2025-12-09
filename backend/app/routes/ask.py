from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AskRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask(req: AskRequest):
    return {"answer": "placeholder"}