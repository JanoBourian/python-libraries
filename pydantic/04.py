# Trying types
from pydantic import BaseModel, validator, PositiveFloat, PositiveInt, StrictStr

class Testing(BaseModel):
    value_string: StrictStr
    
    # Validation for string with out special characters
    @validator("value_string")
    def string_is_alpha(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("One value must containe only letters")
        return v
    
data = {
    "value_string": "mail_esteman@mail.com"
}

Testing(**data)