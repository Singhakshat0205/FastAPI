from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field, json
from typing import List, Dict, Optional, Annotated, Literal
from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse

app= FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data= json.load(f)
    return data

def save_data(data):
    with open('patients.json','w') as f:
            data= json.dump(data, f)



class Patient(BaseModel):

    id:Annotated[str, Field(..., description='Id of patient')]
    name:Annotated[str, Field(..., description='name of the patient')]
    city:Annotated[str, Field(..., description='city of patient')]
    age:Annotated[int, Field(gt=0, lt=100,description='Age of the patient')]
    gender:Annotated[Literal['male','female','other'], Field(..., description='Gender of the patient')]
    weight:Annotated[float, Field(..., gt=0, description='weight of the patient')]
    height:Annotated[float, Field(..., gt=0, description='Height of the patient')]


    
    @computed_field
    @property
    def bmi(self)->float:
        bmi= round(self.weight/(self.height**2),2)

        return bmi


    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<10.5:
            return 'Underweight'
        elif self.bmi <25:
            return 'Normal'
        elif self.bmi<30:
            return 'Normal'
        else:
            return 'obyss'



@app.post('/create')
def create_patient(patient:Patient):

    data= load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    data[patient.id]= patient.model_dump(exclude=['id'])


    save_data(data)


    return JSONResponse(status_code=201, message={'patient created successfully'})