# def insert_patient_data(name:str, age:int):

#     if type(name)==str and type(age)==int:
#         if age<=0:
#             return ValueError('age cannot be zero or negative')
#         print(name)
#         print(age)

#     else:
#         return TypeError('Incorrect data type given')


# ## see with the above code we are able to perform input validation but the above process is very manual and pydantic helps us in this 



from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

##by default all the parameters are required

class Patient(BaseModel):


     
     name:Annotated[str,Field(max_length=30, title='Name of the patient', description='Give the name of the patient in less than 30 words', examples=['Nitish singh', 'Akshat Singh'])]
     #see above now with the help of field we are adding metadata as well as field constraints
     email:EmailStr ## common scenario based data validation
     linkedin_url:AnyUrl= None
     age: int = Field(gt=0)
     weight:Annotated[float , Field(gt=0, strict=True)] ## this is custom data validation 
     married:Annotated[bool, Field(default= None, description='Is the patient married or not')] ## this is also optional with default value as False 
     allergies:Annotated[Optional[List[str]], Field(default= None, max_length=5,description='please mention the allergies of the patient')] ## now this has become an optional field with default value as None
     contact_details: Dict[str, str]


patient_info= {'name':'Akshat','email':'avv@gmail.com','age':30, 'weight':60.6, 'allergies':['pollen','dust'], 'contact_details':{
     'email':'abc@gmail.com',
     'mobile':'8594949999'
}}

patient1= Patient(**patient_info)

def insert_patient_data(patient:Patient):

     print(patient.name)
     print(patient.age)
     print(patient.weight)
     print(patient.allergies)
     print(patient.married)

     print('Inserted')


insert_patient_data(patient1)