from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select
from faker import Faker
from model import Members, Coaches, Accesscards, Registrations, Courses
from init_db import engine
import random
import datetime

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
        given_access=[]
        while len(given_access) < len(access):
            card_id=fake.random_element(access)
            unique_number=fake.random_number(8)
            if card_id in given_access:
                continue
            else:
                given_access.append(card_id)
                w = Accesscards(card_id=card_id,
                        unique_number=unique_number)
                session.add(w)
                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()
accesscards(20)

def coaches(count=11):
    fake=Faker()
    session = Session(engine)
    specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
    i=1
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

def courses(courses_number):
    fake = Faker()
    session = Session(engine)
    specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
    time_plan_list=[]

    with Session(engine):
        statement= select(Coaches.coach_id)
        results = session.exec(
            statement
        )
        access = results.all()
        
        while len(time_plan_list) <courses_number:
            hour=datetime.datetime(2024, 11, random.randint(1,30), random.randint(9,17),0,0)
            if hour in time_plan_list:
                continue
            else:
                y=Courses(course_id=fake.random_number(3),
                card_id=fake.random_element(access),
                course_name=random.choice(specialty_list),
                time_plan=hour,
                max_capacity=fake.random_number(2),
                coach_id=fake.random_element(access)
                )
                time_plan_list.append(hour)
            session.add(y)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
    
courses(20)


def registrations(m):
    fake = Faker()
    session = Session(engine)
    statement= select(Members.member_id)
    results_m = session.exec(
            statement
        )
    access_m = results_m.all()
    statement_c= select(Courses.course_id)
    results_c = session.exec(
            statement_c
        )
    access_c = results_c.all()
    
    for j in range(1, m):
        x=Registrations(registration_id=j,
                registration_date=fake.future_datetime(),
                member_id=fake.random_element(access_m),
                course_id=fake.random_element(access_c)
                )
                
        session.add(x)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
registrations(21)


