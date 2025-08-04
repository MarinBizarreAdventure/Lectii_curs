from pydantic import BaseModel, field_validator
from typing import Optional

class Address(BaseModel):
    street:str
    city: str

class  UserProfile(BaseModel):
    name: str
    age: Optional[int] = None
    

data = '{"name":"marin"}'

user = UserProfile(name="222")

print(user.json())


