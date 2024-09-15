# With Pytdantic stays more easy to declare types of the elements.
# https://docs.pydantic.dev/latest/
# Is a good practice use Pydantic with Fast API, because becomes it more easy to understand what code means.

from datetime import datetime

# from pydantic import BaseModel
from pydantic import BaseModel, PositiveInt, ValidationError


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
# user = User(**external_data)

try:
    user = User(**external_data)  
except ValidationError as e:
    print(e.errors())

print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123