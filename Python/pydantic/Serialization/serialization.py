from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
  street:str
  city:str
  zip_code:str


class User(BaseModel):
  id:int
  name:str
  email:str
  is_active:bool=True
  createdAt:datetime
  address:Address
  tags:List[str]=[]

  model_config=ConfigDict(
    json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}

  )

user=User(
  id=1,
  name="mansi",
  email="m@gmail.com",
  createdAt=datetime(2025, 3, 15, 14, 30,55),
  address=Address(
    street="Something",
    city="Jaipur",
    zip_code="208021"
  ),
  is_active=False,
  tags=["premuim","subscriber"]
)

python_dict=user.model_dump()
print(python_dict)
print("="*30)
print(user)

json_str=user.model_dump_json()
print("="*50)
print(json_str)