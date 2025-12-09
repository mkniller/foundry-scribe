from fastapi import FastAPI
from app.routes import ask

app = FastAPI()
app.include_router(ask.router)

@app.get("/")
def root():
    return {"status": "ok"}