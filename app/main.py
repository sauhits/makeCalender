from fastapi import FastAPI
from pydantic import BaseModel
from drawMonthly import drawCalender
import base64, os


class Tasks(BaseModel):
    day: int
    title: str
    description: str


class CalenderRequest(BaseModel):
    year: int
    month: int
    tasks: list[Tasks]


app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.post("/calender")
async def makeCalender(calender_request: CalenderRequest):
    task_dict: dict[int, str] = await makeTaskDict(calender_request.tasks)
    description_dict: dict[int, str] = await makeDescriptionDict(calender_request.tasks)
    await drawCalender(
        calender_request.year, calender_request.month, task_dict, description_dict
    )
    tmp_path = "/tmp/tmp.jpg"
    with open(tmp_path, "rb") as f:
        image_data: bytes = f.read()

    encoded: bytes = base64.b64encode(image_data)
    os.remove(tmp_path)
    response: list = []
    if encoded != "":
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
