import asyncio

from fastapi import FastAPI
from pydantic import BaseModel

from app.bot import process_query

app = FastAPI()


class QueryRequest(BaseModel):
    query: str
    id: int


@app.post("/api/request")
async def handle_request(request: QueryRequest):
    return await asyncio.to_thread(process_query, request.query, request.id)
