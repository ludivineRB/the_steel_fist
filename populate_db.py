from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select
from faker import Faker
from model import Members, Coaches, Accesscards, Registrations, Courses
from init_db import engine
import random


####################################################################
#WARNING this is fake data without any link between table
####################################################################


def member(count=20):
    fake = Faker()
    session = Session(engine)
    i = 0
    while i < count:
        u = Members(member_id=fake.random_number(4),
                 member_name=fake.name(),
                 email=fake.email(),
                 access_card_id=fake.random_number(4))
        session.add(u)
        try:
            session.commit()
            i += 1
        except IntegrityError:
            session.rollback()
member()

def accesscards(n):
    fake = Faker()
    session = Session(engine)
    with Session(engine):
        statement= select(Members.access_card_id)
        results = session.exec(
            statement
        )
        access = results.all()
        #print(members_list)
        for _ in range(n):
            card_id=fake.random_element(access)
            unique_number=fake.random_number(8)
            w = Accesscards(card_id=card_id,
                    unique_number=unique_number)
            session.add(w)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
accesscards(20)

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

def courses(o):
    fake = Faker()
    session = Session(engine)
    specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]

    with Session(engine):
        statement= select(Coaches.coach_id)
        results = session.exec(
            statement
        )
        access = results.all()
        
        for _ in range(o):
            y=Courses(course_id=fake.random_number(3),
            card_id=fake.random_element(access),
            course_name=random.choice(specialty_list),
            time_plan=fake.future_datetime(),
            max_capacity=fake.random_number(2),
            coach_id=fake.random_element(access)
            )
            session.add(y)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
    
courses(20)


def registrations(m):
    fake = Faker()
    session = Session(engine)
    statement= select(Coaches.coach_id)
    results = session.exec(
            statement
        )
    access = results.all()
        
    for j in range(m):
        x=Registrations(registration_id=j,
                registration_date=fake.future_datetime(),
                member_id=fake.random_number(5),
                course_id=fake.random_number(10)
                )
                
        session.add(x)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
registrations(20)


#check links between tables
#check if we can link courses names with specialty
