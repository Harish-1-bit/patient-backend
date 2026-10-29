from fastapi import FastAPI
from src.utils.db import base,engine
from src.Task.router import task_route

base.metadata.create_all(engine)

app = FastAPI(title='This is Task Management Application')
app.include_router(task_route)