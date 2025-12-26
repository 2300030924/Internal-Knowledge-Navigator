from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.agents.mcp_agent import handle_query

app = FastAPI(title="Internal Knowledge Navigator API",
              description="MCP-style agent for document search, summarization, and comparison.",
              version="1.0")

# Allow CORS (so AgentThink or browser UIs can call it)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def process_query(request: QueryRequest):
    """
    Handle incoming user queries (search, summarize, compare, etc.)
    """
    response = handle_query(request.query)
    return {"query": request.query, "response": response}


@app.get("/")
def root():
    return {"message": "🧠 Internal Knowledge Navigator API is running!"}
