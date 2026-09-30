from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):


    name: str
    email:EmailStr
    age:int
    weight: float
    married: bool
    allergies:List[str]
    contact_details:Dict[str, str]


    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age >60 and 'emergency' not in self.contact_details:
            return ValueError('Patients above 60 should have an emergency contact number')

        return self
 


patient_info = {
    'name': 'Akshat',
    'email': 'avv@hdfc.com',
    'age': 80, 
    'weight': 60.6,
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
    
update_patient_data(patient1)