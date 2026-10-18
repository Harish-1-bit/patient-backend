from fastapi import FastAPI
import json

app =FastAPI() 

def loadData():
    with open('patient.json','r') as f:
        data = json.load(f)
        
    return data

@app.get('/')
def hello():
    return {'message' : 'Patient Management System'}\
    

@app.get('/patients')
def patients():
    data=loadData()
    return data