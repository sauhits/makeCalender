from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Tasks(BaseModel):
    day: int
    title: str
    description: str


class CalenderRequest(BaseModel):
    year: int
    month: int
    tasks: List[Tasks]


# 受けとったjsonをリストにする
json: CalenderRequest = {
    "year": 2026,
    "month": 2,
    "tasks": [
        {"day": 18, "title": "卒論締切", "description": "4年の卒論締切18時"},
        {"day": 3, "title": "飲み会", "description": ""},
    ],
}


app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.get("/calender")
async def makeCalender():
    taskCheck(json)
    return {"message": "Hello, World"}
