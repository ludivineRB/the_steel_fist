from sqlalchemy.exc import IntegrityError
from sqlmodel import Session
from faker import Faker
from model import Members, Coaches
from init_db import engine
import random

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
#members()

def coaches(count=10):
    fake=Faker()
    session = Session(engine)
    specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
    i=0
    while i < count:
        v = Coaches(coach_id=i,
                 coach_name_name=fake.name(),
                 specialty=random.choice(specialty_list))
        session.add(v)
        try:
            session.commit()
            i += 1
        except IntegrityError:
            break
coaches()
