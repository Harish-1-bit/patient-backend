from fastapi import APIRouter, Depends
from src.Task import controller
from src.Task.dtos import TaskSchema
from src.utils.db import get_db

task_route = APIRouter(prefix='/task')

@task_route.post('/')
def create_task(body:TaskSchema, db = Depends(get_db)):
    return controller.create_task(body, db)