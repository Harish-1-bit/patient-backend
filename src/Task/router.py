from fastapi import APIRouter, Depends
from src.Task import controller
from src.Task.dtos import TaskSchema
from src.utils.db import get_db

task_route = APIRouter(prefix='/task')

@task_route.post('/')
def create_task(body:TaskSchema, db = Depends(get_db)):
    return controller.create_task(body, db)

@task_route.get('/')
def get_task(db = Depends(get_db)):
    return controller.get_task(db)

@task_route.get('/{id}')
def get_one_task(id, db = Depends(get_db)):
    return controller.get_one_task(id,db)

@task_route.patch('/{id}')
def update_task(body : TaskSchema ,id :int , db = Depends(get_db)):
    return controller.update_task(body, id, db)

@task_route.delete('/{id}')
def delete_task(id : int, db=Depends(get_db)):
    return controller.delete_task(id,db)