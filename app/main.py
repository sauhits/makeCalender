from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from drawMonthly import drawCalender
import base64, os, io


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
    if not (2000 <= calender_request.year <= 2030):
        raise HTTPException(status_code=404, detail="year must be 2000–2030")
    if not (1 <= calender_request.month <= 12):
        raise HTTPException(status_code=404, detail="month must be 1-12")
    
    task_dict: dict[int, str] = await makeTaskDict(calender_request.tasks)
    description_dict: dict[int, str] = await makeDescriptionDict(calender_request.tasks)
    tmp_byte = io.BytesIO()
    await drawCalender(
        calender_request.year,
        calender_request.month,
        task_dict,
        description_dict,
        tmp_byte,
    )

    encoded: bytes = base64.b64encode(tmp_byte.getvalue()).decode("utf-8")
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
