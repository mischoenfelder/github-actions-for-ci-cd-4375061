from fastapi import FastAPI, HTTPException
import json
from pathlib import Path

Path = Path(__file__).parent 

app = FastAPI()

# Load data from file
with open(Path / "data.json", "r") as f:
    data = json.load(f)


@app.get("/")
async def read_data():
    return data


@app.get("/{guid}")
async def read_data_by_guid(guid: str):
    for item in data:
        if item["guid"] == guid:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
