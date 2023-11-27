from datetime import datetime
from pydantic import BaseModel, PositiveInt

class User(BaseModel):
    user_id:int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]

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

    user = User(**external_data)
    print(user.user_id)
    print(user.tastes)
    
except ValueError as e:
    print(e.errors())