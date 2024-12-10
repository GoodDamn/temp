from pydantic import BaseModel

class EventForm(BaseModel):
    userId: int

class UserAuth(BaseModel):
    username: str
    password: str

class User(UserAuth):
    role: int

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