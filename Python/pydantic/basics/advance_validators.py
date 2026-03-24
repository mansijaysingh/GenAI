from pydantic import BaseModel, field_validator,model_validator
from datetime import datetime

class Person(BaseModel):
  first_name:str
  last_name:str

  @field_validator('first_name', 'last_name')
  def names_must_be_capitalize(cls,v):
    if not v.istitle():
      raise ValueError("Names must be capitalized")
    return v
  
class User(BaseModel):
  email:str

  @field_validator('email')
  def normalize_email(cls,v):
    return v.lower().strip()
  


class Product(BaseModel):
  price:str


  @field_validator('price',mode='before')
  def parse_price(cls,v):
    if isinstance(v,str):
      return float(v.replace('$',''))
    return v
  


class DateRange(BaseModel):
  start_date:datetime
  end_date:datetime

  @model_validator(mode="after")
  def validate_date_range(cls, value):
    if value.start_date >= value.end_date:
      raise ValueError("End date must be after start date")
    return value
  
    


p = Person(first_name="Mansi", last_name="Singh")
print(p)
# p1 = Person(first_name="mansi", last_name="singh")
# print(p1)

u = User(email="  MANSI@GMAIL.COM ")
print(u.email)
# u1= User(email="not-an-email")
# print(u1)


p = Product(price="$100")
print(p.price)
# p1 = Product(price="abc")
# print(p1)