from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select, func
from model import Members, Coaches, Accesscards, Registrations, Courses
from init_db import engine
import datetime

def select_course(course_name):
    with Session(engine) as session:
        statement= select(Courses).where(Courses.course_name==course_name)
        results = session.exec(
            statement
        )
        access = results.all()
    return access
print(select_course("yoga"))