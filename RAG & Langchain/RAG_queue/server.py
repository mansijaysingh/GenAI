from fastapi import FastAPI, Query
from client.rq_client import queue
from my_queue.worker import process_query

app=FastAPI()

@app.get("/")
def root():
  return ("STATUS: server is running")

@app.post("/chat")
def chat(
    query:str=Query(..., description="The chat query of user")
):
  job=queue.enqueue(process_query, query)
  return {"status":"queued", "job_id": job.id}