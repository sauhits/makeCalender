from fastapi import FastAPI
from pydantic import BaseModel
from drawMonthly import drawCalender
import base64


class Tasks(BaseModel):
    day: int
    title: str
    description: str


class CalenderRequest(BaseModel):
    year: int
    month: int
    tasks: list[Tasks]


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


@app.post("/calender/")
async def makeCalender(calender_request: CalenderRequest):
    task_dict: dict[int, str] = await makeTaskDict(calender_request.tasks)
    description_dict: dict[int, str] = await makeDescriptionDict(calender_request.tasks)
    file_path: str = await drawCalender(
        calender_request.year, calender_request.month, task_dict, description_dict
    )
    with open(file_path, "rb") as f:
        image_data: bytes = f.read()

    encoded: bytes = base64.b64encode(image_data)
    response: list = []
    if file_path != "":
        response.append({"res": "ok", "base64": encoded})
        return response
    response.append({"res": "ng"})
    return response


async def makeTaskDict(task_list: list[Tasks]):
    task_dict: dict[int, str] = {}
    for task in task_list:
        task_dict[task.day] = task.title
    return task_dict


async def makeDescriptionDict(task_list: list[Tasks]):
    description_dict: dict[int, str] = {}
    for task in task_list:
        description_dict[task.day] = task.description
    return description_dict
