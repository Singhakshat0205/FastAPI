from pydantic import EmailStr, BaseModel, field_validator, Field


from typing import List, Dict, Optional, Annotated

class Address(BaseModel):

    city:str
    state:str
    pin:str

class Patient(BaseModel):

    name:str
    gender:str
    age:int
    address:Address



address_dict= {'city':'Pune', 'state':'UP', 'pin':'999499'}

address1= Address(**address_dict)


patient_dict= {
    'name':'Akshat',
    'gender':'Male',
    'age':34, 
    'address':address1
}


patient1= Patient(**patient_dict)

print(patient1)
print(patient1.address.pin)

