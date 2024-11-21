from sqlalchemy.exc import IntegrityError
from faker import Faker
from sqlmodel import Session, select, func, delete
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
#print(add_member("toto", "toto@mail", 123456))


def add_coache(name, spe):
    session=Session(engine)
    new_coache=Coaches(coach_name=name, 
                        specialty=spe)
    session.add(new_coache)
    session.commit()
    validation=f"Addition of the new coach {name}"
    return validation
#print(add_coaches("toto", "tennis"))


def add_course(name, date, max_participants, coach_Id):
    session=Session(engine)
    date=datetime.datetime.fromisoformat(date)
    new_course=Courses(course_name=name,
                       time_plan=date,
                       max_capacity=max_participants,
                       coach_id=coach_Id)
    session.add(new_course)
    session.commit()
    validation=f"Addition of the course {name} at {date} with the coach {coach_Id}"
    return validation

#print(add_course("yoga", "2024-11-26 09:00", 10, 3))

def delete_member(name):
    with Session(engine) as session:
        statement= select(Members).where(Members.member_name==name)
        results=session.exec(statement)
        to_delete=results.one()
        session.delete(to_delete)
        session.commit()
        validation=f"The member {name} has been removed from the database"
    return validation
#print(delete_member('Holly Thompson'))

def delete_coach(name):
    with Session(engine) as session:
        statement= select(Coaches).where(Coaches.coach_name==name)
        results=session.exec(statement)
        to_delete=results.one()
        session.delete(to_delete)
        session.commit()
        validation=f"The coach {name} has been removed from the database"
    return validation
#print(delete_coach('Danielle Lewis'))

def delete_course(number):
    with Session(engine) as session:
        statement= select(Courses).where(Courses.course_id==number)
        results=session.exec(statement)
        to_delete=results.one()
        session.delete(to_delete)
        session.commit()
        validation=f"The course {number} has been removed from the database"
    return validation
print(delete_course(1))

def historic_registrations(member_Id):
    statement=select()