import models

from databaseEvents import dbEvents
from databaseApplicantEvents import dbApplicantEvents
from databaseUsers import dbUsers

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database import Database


app = FastAPI(
    title = "Applicants",
    docs_url= "/swagger"
)


@app.post("/login")
def login(model: models.User):

    result = dbUsers().findUsers(
        model.username,
        model.password,
        model.role
    )

    resultLen = len(result)

    if resultLen == 1:
        return JSONResponse(
            result[0][0],
            status_code=200)
    
    return JSONResponse(
        "need to sign in",
        status_code=400)    

@app.post("/signin")
def signin(model: models.User):

    # applicant
    # employee
    if model.role < 0 or model.role > 1:
        return JSONResponse(
            "incorrect role",
            status_code=400)
    
    db = dbUsers()

    db.addUser(
        model.username,
        model.password,
        model.role
    )

    result = db.countUsers()
    
    return JSONResponse(
        result,
        status_code=200
    )

@app.get("/events")
def events():
    return dbEvents().getEvents()

@app.post("/event/{eventId}/create")
def create_event_form(
    eventId: int,
    model: models.EventForm):

    dbApplicantEvents().createForm(
        model.userId,
        eventId
    )

    return JSONResponse(
        status_code=200
    )

@app.post("/event/create")
def create_event(model: models.EventInsert): 
    dbEvents().createEvent(
        model.name,
        model.desc,
        model.register,
        model.date,
        model.university_id
    )
    return 

@app.get("/events/{university_id}")
def listUniversityEvents(
    university_id: int):

    return dbEvents().getEventsByUniversity(
        university_id
    )

@app.get("/event/{id}")
def eventInfo(
    id: int):
    return f"event info {id}"

@app.put("/event/{id}/report")
def create_Event_Report(
    id: int):
    return f"event report {id}"