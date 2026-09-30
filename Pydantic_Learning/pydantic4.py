from pydantic import EmailStr, BaseModel, field_validator, Field, computed_field


from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):


    name:str
    email: EmailStr
    age:int
    weight:float
    height:float
    married:float
    allergies:List[str]
    contact_details:Dict[str, str]


    @computed_field
    @property
    def bmi(self)->float:
        bmi= round(self.weight/(self.height**2),2)

        return bmi



patient_info = {
    'name': 'Akshat',
    'email': 'avv@hdfc.com',
    'age': 80, 
    'weight': 60.6,
    'height':77.6,
    'married': True,
    'allergies': ['pollen', 'dust'], 
    'contact_details': {
        'email': 'abc@gmail.com', 
        'mobile': '8594949999'
    }
}

patient1= Patient(**patient_info)

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    
update_patient_data(patient1)