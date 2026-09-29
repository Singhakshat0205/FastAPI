from pydantic import EmailStr, BaseModel, field_validator, Field


from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):


    name:str
    email: EmailStr
    age:int
    weight:float
    married:Annotated[bool, Field(default=None)]
    allergies:List[str]
    contact_details:Dict[str, str]



    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains= ['hdfc.com','icici.com','pnb.com']
        domain_name= value.split('@')[-1]


        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')

        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    # if mode is before then the value in the method will be getting before type conversion on that data type but for mode equals after value is already type converted
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0< value <100:
            return True

        else:
            raise ValueError('Age should be entered as numbers')


patient_info= {'name':'Akshat','email':'avv@hdfc.com','age':'30', 'weight':60.6, 'allergies':['pollen','dust'], 'contact_details':{
     'email':'abc@gmail.com',
     'mobile':'8594949999'
}}

patient1= Patient(**patient_info)

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    print(patient.weight)
    
update_patient_data(patient1)