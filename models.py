from pydantic import BaseModel

class University(BaseModel):
    name: str
    desc: str

class EventForm(BaseModel):
    userId: int

class UserAuth(BaseModel):
    username: str
    password: str

class User(UserAuth):
    role: int

class UserInfo(BaseModel):
    firstName: str
    secondName: str
    surname: str
    isMale: bool

class EventInsert(BaseModel):
    name: str
    desc: str
    register: bool
    date: int
    university_id: int

class Event(BaseModel):
    id: int
    name: str
    desc: str
    register: bool
    event_date: str