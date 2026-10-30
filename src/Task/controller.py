from src.Task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.Task.models import TaskModel
from fastapi import HTTPException

def create_task(body:TaskSchema, db:Session):
    data = body.model_dump()
    new_task = TaskModel(title= data['title'],description = data['description'], is_completed = data['is_completed'])
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {'status':201, 'data':new_task}


def get_task(db:Session):
    task = db.query(TaskModel).all()
    return {'status':200, 'data':task }


def get_one_task(id:int, db:Session):
    task = db.query(TaskModel).get(id)
    if not task:
        raise  HTTPException(404, detail='Task not Found')
    return {'status':200, 'data':task}


def update_task(body : TaskSchema ,id:int, db:Session):
    task = db.query(TaskModel).get(id)
    if not task:
        raise HTTPException(404, detail='task id may be incorrect or task may be not found')
    task.title = body.title
    task.description = body.description
    task.is_completed = body.is_completed
    db.commit()
    db.refresh(task)
    return {'status' : 200, 'data':task}


def delete_task(id:int , db:Session):
    task = db.query(TaskModel).get(id)
    if not task:
            raise HTTPException(404, detail='task id may be incorrect or task may be not found')
    db.delete(task)
    db.commit()
    return {'status':200, 'message':'task successfully deleted'}