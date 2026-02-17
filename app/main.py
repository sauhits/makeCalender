from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from drawMonthly import drawCalender
import base64, io
from fastapi.middleware.cors import CORSMiddleware


class Tasks(BaseModel):
    day: int
    title: str
    description: str


class CalenderRequest(BaseModel):
    year: int
    month: int
    tasks: list[Tasks]


app = FastAPI()

origins = [
    "https://sauhits.github.io",
    "http://localhost:8000",  # ローカル開発用
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.post("/calender")
async def makeCalender(calender_request: CalenderRequest):
    if not (2000 <= calender_request.year <= 2030):
        raise HTTPException(status_code=400, detail="year must be 2000–2030")
    if not (1 <= calender_request.month <= 12):
        raise HTTPException(status_code=400, detail="month must be 1-12")
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
        if not (1 <= task.day <= 31):
            raise HTTPException(status_code=400, detail="day must be 1-31")
        if 7 < len(task.title):
            raise HTTPException(status_code=400, detail="task title too long (MAX:7)")
        task_dict[task.day] = task.title
    return task_dict


async def makeDescriptionDict(task_list: list[Tasks]):
    description_dict: dict[int, str] = {}
    for task in task_list:
        if not (1 <= task.day <= 31):
            raise HTTPException(status_code=400, detail="day must be 1-31")
        if 30 < len(task.description):
            raise HTTPException(
                status_code=400, detail="task description too long (MAX:30)"
            )
        description_dict[task.day] = task.description
    return description_dict
