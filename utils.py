from sqlalchemy.exc import IntegrityError
from faker import Faker
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
#print(select_course("yoga"))

def add_member(name, mail, access):
    fake=Faker()
    session=Session(engine)
    new_member=Members(member_name=name,
                       email=mail,
                       access_card_id=access)
    new_card=Accesscards(card_id=access,
                         unique_number=fake.random_number(6))
    session.add(new_member) 
    session.add(new_card)
    session.commit()
    validation=f"Addition of the new member {name}"
    return validation

# print(add_member("toto", "toto@mail", 123456))
def add_coaches(name, spe):
    session=Session(engine)
    new_coaches=Coaches(coach_name=name, 
                        specialty=spe)
    session.add(new_coaches)
    session.commit()
    validation=f"Addition of the new coach: {name}"
    return validation
#print(add_coaches("toto", "tennis"))

