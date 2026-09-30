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


temp= patient1.model_dump()
print(temp)## give you the whole input data as dictionary format



## we can also export some selected fields from the input patient model

temp1=patient1.model_dump(include=['name', 'gender'])

## we can also exclude some fields as below
temp2= patient1.model_dump(exclude=['gender'])
print(temp2)
## or we can do it for nested models

temp3= patient1.model_dump(exclude={'address':['state']})

print(temp3)

temp4= patient1.model_dump(exclude_unset=True)
print(temp4)
##with above those fields will not be  exported for which the values were not set and they have a default value in them 
