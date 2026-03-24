from pydantic import BaseModel
from typing import Optional,List, Union


class Address(BaseModel):
  street:str
  city:str
  postal_code:str

class Company(BaseModel):
  name:str
  address:Optional[Address]=None


class Employee(BaseModel):
  name:str
  company:Optional[Company]=None


class TextContent(BaseModel):
  type:str="text"
  content:str

class ImageContent(BaseModel):
  type:str="Image"
  url:str
  alt_text:str


class Article(BaseModel):
  title:str
  section:List[Union[TextContent,ImageContent]]


class Country(BaseModel):
  name:str
  code:str


class State(BaseModel):
  name:str
  country:Country

class City(BaseModel):
  name:str
  state:State

class Address2(BaseModel):
  street:str
  city:City
  postal_code:str


class Organization(BaseModel):
  name:str
  haed_quarter:Address2
  branches:List[Address2]=[]


emp = Employee(
    name="Mansi",
    company={
        "name": "OpenAI",
        "address": {
            "street": "MG Road",
            "city": "Delhi",
            "postal_code": "110001"
        }
    }
)

print(emp)

article = Article(
    title="My Blog",
    section=[
        {"type": "text", "content": "Hello world"},
        {
            "type": "Image",
            "url": "https://example.com/img.png",
            "alt_text": "sample image"
        }
    ]
)

print(article)


addr = Address2(
    street="Street 1",
    city={
        "name": "Kanpur",
        "state": {
            "name": "UP",
            "country": {
                "name": "India",
                "code": "IN"
            }
        }
    },
    postal_code="208001"
)

print(addr)

org = Organization(
    name="Tech Corp",
    head_quarter={
        "street": "HQ Street",
        "city": {
            "name": "Mumbai",
            "state": {
                "name": "Maharashtra",
                "country": {
                    "name": "India",
                    "code": "IN"
                }
            }
        },
        "postal_code": "400001"
    },
    branches=[]
)

print(org)

org = Organization(
    name="Tech Corp",
    head_quarter={
        "street": "HQ Street",
        "city": {
            "name": "Mumbai",
            "state": {
                "name": "Maharashtra",
                "country": {
                    "name": "India",
                    "code": "IN"
                }
            }
        },
        "postal_code": "400001"
    },
    branches=[]
)

print(org)