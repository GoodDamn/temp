import models

from databaseEvents import dbEvents
from databaseApplicantEvents import dbApplicantEvents
from databaseUsers import dbUsers
from databaseUniversities import dbUniversities

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database import Database


app = FastAPI(
    title = "Applicants",
    docs_url= "/swagger"
)

dbEvents().createTable()
dbApplicantEvents().createTable()
dbUsers().createTable()
dbUniversities().createTable()

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

@app.get("/user/{userId}")
def user_info(
    id: int):
    return JSONResponse(
        dbUsers().getUserInfoById(
            id=id
        ),
        status_code=200
    )

@app.get("/events")
def events():
    return JSONResponse(
        dbEvents().getEvents(),
        status_code=200
    )

@app.get("/event/{eventId}/check/{userId}")
def check_form(
    eventId: int,
    userId: int):

    hasUserForm = dbApplicantEvents().hasUserForm(
        eventId=eventId,
        userId=userId
    )

    if hasUserForm:
        return JSONResponse(
            None,
            status_code=200
        ) 

    return JSONResponse(
        None,
        status_code=404
    )

@app.post("/event/{eventId}/create")
def create_event_form(
    eventId: int,
    model: models.EventForm):

    dbApplicantEvents().createForm(
        model.userId,
        eventId
    )

    return JSONResponse(
        "Запись успешна",
        status_code=200
    )

@app.post("/event/create")
def create_event(model: models.EventInsert): 
    dbEvents().createEvent(
        model.name,
        model.desc,
        model.register,
        model.university_id,
        model.date
    )
    return JSONResponse(
        None,
        status_code=200
    )

@app.get("/events/{university_id}")
def get_university_events(
    university_id: int):

    return JSONResponse(
        dbEvents().getEventsByUniversity(
            university_id
        ),
        status_code=200
    )

@app.delete("/event/{id}")
def delete_event(
    id: int):
    dbEvents().deleteEventById(
        id
    )

    return JSONResponse(
        None,
        status_code=200
    )

@app.get("/event/{id}")
def event_info(
    id: int):
    return JSONResponse(
        dbEvents().getEventById(
            id
        ),
        status_code=200
    )

@app.get("/universities")
def universities():
    return JSONResponse(
        dbUniversities().getUniversities(),
        status_code=200
    )

@app.get("/university/{id}")
def university_info(id: int):
    return JSONResponse(
        dbUniversities().getUniversityById(
            id
        ),
        status_code=200
    )

@app.post("/university/create")
def create_university(
    model: models.University):
    dbUniversities().createUniversity(
        model.name,
        model.desc
    )

    return JSONResponse(
        None,
        status_code=200
    )