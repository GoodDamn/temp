from fastapi import FastAPI
from repo import Database

import models

app = FastAPI(
    title = "Applicants",
    docs_url= "/swagger"
)
d = Database()
d.query(
    '''create table if not exists events (
        id integer primary key autoincrement,
        name string,
        desc string,
        register bool,
        event_date int
        );
    '''
)

d.query(
    '''create table if not exists users (
        id integer primary key autoincrement,
        username string,
        password string,
        date_register int
        );
    '''
)

@app.post("/login")
def login(model: models.User):
    cursor = Database().query(
        f'''
        select id from users where
            username = \"{model.username}\" and
            password = \"{model.password}\"
        '''
    )

    result = cursor.fetchall()
    resultLen = len(result)

    if resultLen == 1:
        return result[0][0]

    if resultLen == 0:
        return "need to sign in"    

    return None

@app.post("/signin")
def signin(model: models.User):
    Database().query(
        f'''
        insert into users (
            username,
            password,
            date_register
        ) values (
            \"{model.username}\",
            \"{model.password}\",
            DateTime('now')
        );
        '''
    )
    return 

@app.get("/events")
def events():

    out = []
    result = Database().select("events")

    for row in result:
        out.append(
            {
                "id": row[0],
               "name": row[1],
                "desc": row[2],
                "register": row[3],
                "date": row[4]
            }
        )

    return str(out)

@app.put("/event/{id}/create")
def createEventForm(
    id: int):



    return f"event {id}"

@app.post("/event/create")
def create_event(model: models.EventInsert): 
    Database().query(
        f'''
        insert into events (
            name,
            desc,
            register,
            event_date
        ) values (
            '{model.name}',
            '{model.desc}',
            {model.register},
            {model.date}
        );
        '''
    )
    return 

@app.put("/event/applicant/{user_id}")
def sendEventForm(
    user_id: int):
    return f"applicant {user_id}"

@app.get("/events/{university_id}")
def listUniversityEvents(
    university_id: int):
    return f"university events {university_id}"

@app.get("/event/{id}")
def eventInfo(
    id: int):
    return f"event info {id}"

@app.put("/event/{id}/report")
def create_Event_Report(
    id: int):
    return f"event report {id}"