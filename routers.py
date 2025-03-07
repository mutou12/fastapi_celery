from fastapi import APIRouter, HTTPException
from task import add, mul, xsum
from pydantic import BaseModel
from app_factory import create_app
from fastapi.encoders import jsonable_encoder
import logging
import os
# 进行日志配置

api_router = APIRouter()

class AddTask(BaseModel):
    x: int
    y: int

class MulTask(BaseModel):
    x: int
    y: int

class XSumTask(BaseModel):
    numbers: list[int]

@api_router.get("/health-check")
def health_check():
    return {"status": "ok"}

@api_router.post("/tasks/add")
def run_add_task(task: AddTask):
    task = add.apply_async((task.x, task.y))
    return {"task_id": task.id}

@api_router.post("/tasks/mul")
def run_mul_task(task : MulTask):
    task = mul.apply_async((task.x, task.y))
    return {"task_id": task.id}

@api_router.post("/tasks/xsum")
def run_xsum_task(task: XSumTask):
    task = xsum.apply_async((task.numbers,))
    return {"task_id": task.id}

@api_router.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    app=create_app()
    task = app.celery.AsyncResult(task_id)    
    if task.state == 'PENDING':
        return {"task_id": task.id, "state": task.state}
    elif task.state != 'FAILURE':
        return {"task_id": task.id, "state": task.state, "result": task.result}
    else:
        return {"task_id": task.id, "state": task.state, "error": str(task.info)}