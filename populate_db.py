from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select
from faker import Faker
from model import Members, Coaches, Accesscards, Registrations, Courses
from init_db import engine
import random
import datetime

# def member(count=20):
#     fake = Faker()
#     session = Session(engine)
#     i = 0
#     while i < count:
#         u = Members(member_id=fake.random_number(4),
#                  member_name=fake.name(),
#                  email=fake.email(),
#                  access_card_id=fake.random_number(4))
#         session.add(u)
#         try:
#             session.commit()
#             i += 1
#         except IntegrityError:
#             session.rollback()
# member()

# def accesscards(n):
#     fake = Faker()
#     session = Session(engine)
#     with Session(engine):
#         statement= select(Members.access_card_id)
#         results = session.exec(
#             statement
#         )
#         access = results.all()
#         given_access=[]
#         while len(given_access) < len(access):
#             card_id=fake.random_element(access)
#             unique_number=fake.random_number(8)
#             if card_id in given_access:
#                 continue
#             else:
#                 given_access.append(card_id)
#                 w = Accesscards(card_id=card_id,
#                         unique_number=unique_number)
#                 session.add(w)
#                 try:
#                     session.commit()
#                 except IntegrityError:
#                     session.rollback()
# accesscards(20)

# def coaches(count=11):
#     fake=Faker()
#     session = Session(engine)
#     specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
#     i=1
#     while i < count:
#         v = Coaches(coach_id=i,
#                  coach_name=fake.name(),
#                  specialty=random.choice(specialty_list))
#         session.add(v)
#         try:
#             session.commit()
#             i += 1
#         except IntegrityError:
#             session.rollback()
# coaches()

# def courses(courses_number):
#     fake = Faker()
#     session = Session(engine)
#     specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
#     time_plan_list=[]

#     with Session(engine):
#         statement= select(Coaches.coach_id)
#         results = session.exec(
#             statement
#         )
#         access = results.all()
        
#         while len(time_plan_list) <courses_number:
#             hour=datetime.datetime(2024, 11, random.randint(1,30), random.randint(9,17),0,0)
#             if hour in time_plan_list:
#                 continue
#             else:
#                 y=Courses(course_id=fake.random_number(3),
#                 card_id=fake.random_element(access),
#                 course_name=random.choice(specialty_list),
#                 time_plan=hour,
#                 max_capacity=fake.random_number(2),
#                 coach_id=fake.random_element(access)
#                 )
#                 time_plan_list.append(hour)
#             session.add(y)
#             try:
#                 session.commit()
#             except IntegrityError:
#                 session.rollback()
    
# courses(20)


# def registrations(m):
#     fake = Faker()
#     session = Session(engine)
#     statement= select(Members.member_id)
#     results_m = session.exec(
#             statement
#         )
#     access_m = results_m.all()
#     statement_c= select(Courses.course_id)
#     results_c = session.exec(
#             statement_c
#         )
#     access_c = results_c.all()
    
#     for j in range(1, m):
#         x=Registrations(registration_id=j,
#                 registration_date=fake.future_datetime(),
#                 member_id=fake.random_element(access_m),
#                 course_id=fake.random_element(access_c)
#                 )
                
#         session.add(x)
#         try:
#             session.commit()
#         except IntegrityError:
#             session.rollback()
# registrations(21)


# from faker import Faker
# from sqlmodel import Session, select
# from sqlalchemy.exc import IntegrityError
# import random
# import datetime

def create_members(count=20):
    fake = Faker()
    with Session(engine) as session:
        for _ in range(count):
            member = Members(
                member_name=fake.name(),
                email=fake.email()
            )
            session.add(member)
        session.commit()

def create_accesscards():
    fake = Faker()
    with Session(engine) as session:
        members = session.exec(select(Members)).all()
        for member in members:
            accesscard = Accesscards(
                unique_number=fake.random_number(digits=8),
                member=member
            )
            session.add(accesscard)
        session.commit()

def create_coaches(count=11):
    fake = Faker()
    specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
    with Session(engine) as session:
        for _ in range(count):
            coach = Coaches(
                coach_name=fake.name(),
                specialty=random.choice(specialty_list)
            )
            session.add(coach)
        session.commit()

def create_courses(count=20):
    fake = Faker()
    specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
    with Session(engine) as session:
        coaches = session.exec(select(Coaches)).all()
        for _ in range(count):
            course = Courses(
                course_name=random.choice(specialty_list),
                time_plan=fake.future_datetime(),
                max_capacity=fake.random_int(min=10, max=30),
                coach=random.choice(coaches)
            )
            session.add(course)
        session.commit()

def create_registrations(count=50):
    fake = Faker()
    with Session(engine) as session:
        members = session.exec(select(Members)).all()
        courses = session.exec(select(Courses)).all()
        for _ in range(count):
            registration = Registrations(
                registration_date=fake.date_between(start_date='-1y', end_date='today'),
                member=random.choice(members),
                course=random.choice(courses)
            )
            session.add(registration)
        session.commit()

if __name__ == "__main__":
    create_members()
    create_accesscards()
    create_coaches()
    create_courses()
    create_registrations()