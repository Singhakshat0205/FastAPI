
import fastapi,json
from fastapi import Path , HTTPException, Query
app = fastapi.FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data= json.load(f)
    return data

@app.get("/")
def hello():
    return {'message':'Patient Management API'}


@app.get("/about")
def about():
    return {'message':'A fully functional API to manage the patient records'}


@app.get("/view")
def view():
    return load_data()

@app.get("/sort")
def sort_patients(sort_by: str= Query(..., description='Sort on the basis of height, weight or BMI'), order: str=Query('asc', description='sort in asc or desc order')):

    valid_fields= ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail= f'Invalid field selected from {valid_fields}')

    if order not in ['asc', 'desc']:

        raise HTTPException(status_code=404,
                detail='Invalid order selected between asc and desc')

    data= load_data()

    sort_order= True if order=='asc' else False

    sorted_data= sorted(data.values(), key= lambda x:x.get(sort_by,0), reverse=sort_order)

    return sorted_data
 



@app.get("/view/{patient_id}")
def ViewById(patient_id:str= Path(..., description='Id of the patient in the DB', example='P001')):
    data= load_data()
    if id in data:
        return data[id]
    raise HTTPException(status_code=404, detail='Patient not found')



@app.delete("/delete_patient/{id}")
def PatientDeletion(id:str= Path(..., description='provide the patient id to delete'), example='P001'):

    data= load_data()

    if id in data:
        deleted_patient= data.pop(id)
        return {'message':f'{deleted_patient} got deleted from the patients list'}
    raise HTTPException(status_code=404, detail='cannot find any patient with this id')

# now we will build post and put endpoints of our API

