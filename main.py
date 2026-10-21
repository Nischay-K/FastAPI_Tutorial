from fastapi import FastAPI , Path , HTTPException , Query
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
    raise HTTPException(status_code = 404 , detail = 'Patient not found')

@app.get('/sort')
def sort(sort_by: str = Query(... , description = 'Sort on the basis of height, weight or BMI') , order: str = Query('asc' , description = 'Order by Ascending or Descending order')):
    valid_field = ['height' , 'weight' , 'bmi']

    if sort_by not in valid_field:
        raise HTTPException(status_code = 400 , detail = f'Invalid field select from {valid_field}')

    if order not in ['asc' , 'desc']:
        raise HTTPException(status_code = 400 , detail = f'Invalid field select between ascending or descending')

    data = load_dataset()

    sort_order = True if order == 'desc' else False

    sort_data = sorted(data.values() , key = lambda x : x.get(sort_by , 0) , reverse = sort_order)

    return sort_data