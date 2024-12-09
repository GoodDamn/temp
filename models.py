from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str

class EventInsert(BaseModel):
    name: str
    desc: str
    register: bool
    date: int

class Event(BaseModel):
    id: int
    name: str
    desc: str
    register: bool
    event_date: str