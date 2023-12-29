from datetime import datetime
from pydantic import BaseModel, PositiveInt
from typing import Optional

class User(BaseModel):
    user_id:int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]

class SpecificData(BaseModel):
    age: Optional[int]
class Dictionary(BaseModel):
    user_id: int

try:
    external_data = {
    "user_id":123,
    "name": "Joker",
    "signup_ts": "1990-09-19 09:15:00",
    "tastes": {
        "wine": 9,
        b"cheese": 7,
        "cabbage": "1"
    }
}

    user = User(**external_data)
    print(user.user_id)
    print(user.tastes)
    print(user.tastes.get("wine"))
    
    external_data = {
    "user_id":"Not A Number",
    "name": "Joker",
    "signup_ts": "1990-09-19 09:15:00",
    "tastes": {
        "wine": 9,
        b"cheese": 7,
        "cabbage": "1"
    }
}

    # user = User(**external_data)
    # print(user.user_id)
    # print(user.tastes)
    
    print("### Testing Specific Data")
    data_to_test = {
        "user_id": 1928,
        "nested_dict":
            {
                "bad_age": 10
            }
    }
    
    dictionary = Dictionary(**data_to_test)
    print(dictionary)
    
except ValueError as e:
    print(e.errors())