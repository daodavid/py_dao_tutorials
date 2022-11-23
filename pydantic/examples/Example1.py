import json
from typing import List, Any

from pydantic import BaseModel, ValidationError, validator


class Employee(BaseModel):
    id: int
    name: str
    age: int

    @validator('name')
    def name_must_contain_space(cls, v):
       return v

    @property
    def info(self):
        return f'{str(self.id)} " :::: "  {self.name}'


emp1 = Employee(id=1, name='Krishna', age=23)
empDict = emp1.dict()

print(emp1.info)
print('empDict ' + str(empDict))

u2 = {
    "id": "2",
    "name": " david",
    "age": 12
}
print(*u2)

emp2 = Employee(**u2)
print(emp2)


class Config(BaseModel):
    url: str
    password: str
    user: str


with open('config.json') as f:
    data = json.load(f)
    data : Config = Config(**data)
    print(data.password)
    #print(data.info)




def send(ls : List[Any]) -> None :
    pass