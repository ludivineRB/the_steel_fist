from sqlalchemy.exc import IntegrityError
from sqlmodel import Session
from faker import Faker
from model import Members, Coaches, AccessCards, Registrations, Courses
from init_db import engine
import random


####################################################################
#WARNING this is fake data without any link between table
####################################################################


def members(count=20):
    fake = Faker()
    session = Session(engine)
    i = 0
    while i < count:
        u = Members(member_id=i,
                 member_name=fake.name(),
                 email=fake.email(),
                 access_card_id=fake.phone_number())
        session.add(u)
        try:
            session.commit()
            i += 1
        except IntegrityError:
            session.rollback()
members()

def coaches(count=10):
    fake=Faker()
    session = Session(engine)
    specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
    i=0
    while i < count:
        v = Coaches(coach_id=i,
                 coach_name=fake.name(),
                 specialty=random.choice(specialty_list))
        session.add(v)
        try:
            session.commit()
            i += 1
        except IntegrityError:
            session.rollback()
coaches()

def accesscards(n):
    fake = Faker()
    session = Session(engine)
    for _ in range(n):
        card_id=fake.credit_card_number()
        unique_number=fake.port_number()
        w = AccessCards(card_id=card_id,
                 unique_number=unique_number)
        session.add(w)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
accesscards(20)

def registrations(m):
    fake = Faker()
    session = Session(engine)
    for j in range(m):
        x=Registrations(registration_id=j,
                registration_date=fake.date_object(),
                member_id=fake.random_number(5),
                course_id=fake.random_number(10)
                )
                
        session.add(x)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
registrations(20)

def courses(o):
    fake = Faker()
    session = Session(engine)
    specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
    for _ in range(o):
        y=Courses(course_id=fake.random_number(3),
                course_name=random.choice(specialty_list),
                time_plan=fake.date_object(),
                max_capacity=fake.random_number(2),
                coach_id=fake.random_number(1)
                )
        session.add(y)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
courses(20)

#check links between tables
#check if we can link courses names with specialty
