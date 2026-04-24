from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import retrieve_context
from app.mock_llm import generate_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, OPTIONS, etc.
    allow_headers=["*"],
)

class Query(BaseModel):
    text: str

@app.post("/api/coach")
def coach(query: Query):

    context = retrieve_context(query.text)

    result = generate_response(query.text, context)

    # IMPORTANT: preserve full structure
    return result

@app.get("/api/health")
def health():
    return {"status": "ok"}