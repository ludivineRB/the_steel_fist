from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select, func
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
                max_capacity=10,
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
    with Session(engine) as session:
        fake = Faker()
        # Précharger tous les IDs des membres
        access_m = [member for member in session.exec(select(Members.member_id)).all()]

        # Précharger tous les IDs des cours
        access_c = [course for course in session.exec(select(Courses.course_id)).all()]

        # Récupérer les cours avec leur nombre actuel de participants
        statement = (
            select(Registrations.course_id, func.count(Registrations.member_id).label('nb_participants'))
            .group_by(Registrations.course_id)
        )
        course_participants = {
            row.course_id: row.nb_participants for row in session.exec(statement).all()
        }

        # Initialiser les cours non encore enregistrés dans `Registrations` à 0 participants
        for course_id in access_c:
            if course_id not in course_participants:
                course_participants[course_id] = 0

        # Ajouter des inscriptions de manière aléatoire
        for _ in range(m):
            # Sélectionner un cours aléatoire avec moins de 3 participants
            available_courses = [course_id for course_id, count in course_participants.items() if count < 10]
            if not available_courses:
                print("Tous les cours sont pleins. Impossible d'ajouter plus d'inscriptions.")
                break

            random_course = random.choice(available_courses)
            random_member = fake.random_element(access_m)

            # Créer une nouvelle inscription
            new_registration = Registrations(
                registration_date=fake.future_datetime(),
                member_id=random_member,
                course_id=random_course
            )

            session.add(new_registration)

            try:
                session.commit()
                # Mettre à jour localement le nombre de participants pour le cours choisi
                course_participants[random_course] += 1
            except IntegrityError:
                session.rollback()
                print(f"Conflit d'intégrité lors de l'inscription du membre {random_member} au cours {random_course}.")
registrations(100)
#add a random number of capacity and get this number in each course_id to check now.