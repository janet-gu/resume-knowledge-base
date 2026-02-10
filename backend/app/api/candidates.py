from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for candidates
candidates = {}

class Candidate(BaseModel):
    id: int
    name: str
    experience: str
    skills: list

@app.post("/candidates/", response_model=Candidate)
async def create_candidate(candidate: Candidate):
    if candidate.id in candidates:
        raise HTTPException(status_code=400, detail="Candidate already exists")
    candidates[candidate.id] = candidate
    return candidate

@app.get("/candidates/", response_model=list[Candidate])
async def list_candidates():
    return list(candidates.values())

@app.get("/candidates/{candidate_id}", response_model=Candidate)
async def get_candidate(candidate_id: int):
    if candidate_id not in candidates:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return candidates[candidate_id]

@app.put("/candidates/{candidate_id}", response_model=Candidate)
async def update_candidate(candidate_id: int, candidate: Candidate):
    if candidate_id not in candidates:
        raise HTTPException(status_code=404, detail="Candidate not found")
    candidates[candidate_id] = candidate
    return candidate

@app.delete("/candidates/{candidate_id}")
async def delete_candidate(candidate_id: int):
    if candidate_id not in candidates:
        raise HTTPException(status_code=404, detail="Candidate not found")
    del candidates[candidate_id]
    return {"detail": "Candidate deleted successfully"}
