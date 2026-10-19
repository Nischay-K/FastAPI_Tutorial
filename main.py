from fastapi import FastAPI , Path
import json

app = FastAPI()


def load_dataset():
    with open('patients.json' , 'r') as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {'message' : 'Patient Management System API'}


@app.get('/about')
def about():
    return {'message' : 'A fully functional API to manage your patients record!!'}


@app.get('/view')
def view():
    data = load_dataset()

    return data 

@app.get('/patients/{patient_id}')
def view_patient(patient_id : str = Path(..., description = "ID of the Patient in the DataBase" , example = "P001")):
    data = load_dataset()

    if patient_id in data:
        return data[patient_id]
    return {'error' : 'Sorry! Patient not Found!!'}