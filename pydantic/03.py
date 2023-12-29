from typing import Optional, Union
from pydantic import BaseModel, validator
import datetime


class AccountInformation(BaseModel):
    clabe: str
    is_principal: bool
    
    # Validation for string with out special characters
    @validator("clabe")
    def string_is_alpha(cls, v):
        if not v.replace(" ", "").isnumeric():
            raise ValueError("One value must containe only numbers")
        return v

    @validator("is_principal")
    def verify_if_exists(cls, v):
        if not isinstance(v, bool):
            raise ValueError(f"is_principal is not a boolean, the current value is {type(v)}")
        return v


class Body(BaseModel):
    user_id: int
    updatedAt: datetime.datetime = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d  %H:%M:%S")
    pastPrincipal: AccountInformation = AccountInformation(clabe="1", is_principal = False)
    lastPrincipal: AccountInformation

    # Validation for values that will be received as integers
    @validator("user_id")
    def integer_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("One value must be positive")
        return v

    @validator("user_id")
    def integer_must_be_numeric(cls, v):
        if not isinstance(v, int):
            raise ValueError("One value must be numeric not string or another type")
        return v

information = {
    #   "pastPrincipal":{
    #      "clabe":"014580567403900497",
    #      "is_principal":False
    #   },
      "lastPrincipal":{
         "clabe":"012580015007610747",
         "is_principal":True
      },
      "user_id":2315
   }

body = Body(**information)
print(f"BODY: {body}")
print(f"CLABE: {body.pastPrincipal.clabe}")