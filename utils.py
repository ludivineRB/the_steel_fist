from sqlalchemy.exc import IntegrityError
from faker import Faker
from sqlmodel import Session, select, func, delete, and_, update
from model import Members, Coaches, Accesscards, Registrations, Courses
from init_db import engine
import datetime
import pandas as pd

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
#print(delete_course(2))

#return the number of registration for a person
def historic_number_registrations(name):
    with Session(engine) as session:
        statement=(select(Members.member_id).where(Members.member_name==name))
        name_id =session.exec(statement).first()
        statementh = select(func.count(Registrations.registration_id)).where(Registrations.member_id == name_id)
        result = session.exec(statementh).one()  # Obtenir une valeur scalaire
        return result
print(historic_number_registrations("Jessica Price MD"))

#return the number of registration for a person
def historic_registrations(name):
    with Session(engine) as session:
        statement=(select(Members.member_id).where(Members.member_name==name))
        name_id =session.exec(statement).first()
        statementh = select(Registrations).where(Registrations.member_id == name_id)
        result = session.exec(statementh).all()  
        return result
print(historic_registrations("Jessica Price MD"))

def courses_week(date_begin, date_end):
    with Session(engine) as session:
        date_begin=datetime.datetime.fromisoformat(date_begin)
        date_end=datetime.datetime.fromisoformat(date_end)
        statement =(select(Courses).where(and_(Courses.time_plan > date_begin, Courses.time_plan < date_end)))
        result = session.exec(statement).all()  
        data = [row.__dict__ for row in result]
        for entry in data:
            entry.pop('_sa_instance_state', None)
        df = pd.DataFrame(data)
        df.index = df.index + 1
        return df
  
#print(courses_week("2024-11-01","2024-11-08"))  

def update_course(course_id, new_specialty=None, new_date=None, new_coach_id=None, new_max_participants=None):
    with Session(engine) as session:
        # Préparer les champs à mettre à jour dynamiquement
        updates = {}
        if new_specialty is not None:
            updates["course_name"] = new_specialty
        if new_date is not None:
            updates["time_plan"] = new_date
        if new_coach_id is not None:
            updates["coach_id"] = new_coach_id
        if new_max_participants is not None:
            updates["max_participants"] = new_max_participants

        if not updates:
            return "No fields to update."
        stmt = (
                update(Courses)
                .where(Courses.course_id == course_id)
                .values(**updates)
            )
        # Exécuter la requête
        result = session.exec(stmt)
        session.commit()

        # Vérifier si une ligne a été modifiée
        if result.rowcount == 0:
            return f"No course with ID {course_id} was found."
        return f"Course ID {course_id} updated successfully!"
    
#print(update_course(21, "zumba"))

def update_members(member_id, new_name=None, new_mail=None):
        # Préparer les champs à mettre à jour dynamiquement
        session=Session(engine)
        updates = {}
        if new_name is not None:
            updates["member_name"] = new_name
        if new_mail is not None:
            updates["email"] = new_mail

        if not updates:
            return "No fields to update."
        stmt = (
                update(Members)
                .where(Members.member_id == member_id)
                .values(**updates)
            )
        # Exécuter la requête
        result = session.exec(stmt)
        session.commit()

        # Vérifier si une ligne a été modifiée
        if result.rowcount == 0:
            return f"No member with ID {member_id} was found."
        return f"Member ID {member_id} updated successfully!"
    
#print(update_members(20, "Ludivine"))

def update_coach(coach_id, new_name=None, new_specialty=None):
        # Préparer les champs à mettre à jour dynamiquement
        session=Session(engine)
        updates = {}
        if new_name is not None:
            updates["coach_name"] = new_name
        if new_specialty is not None:
            updates["specialty"] = new_specialty

        if not updates:
            return "No fields to update."
        stmt = (
                update(Coaches)
                .where(Coaches.coach_id == coach_id)
                .values(**updates)
            )
        # Exécuter la requête
        result = session.exec(stmt)
        session.commit()

        # Vérifier si une ligne a été modifiée
        if result.rowcount == 0:
            return f"No coach with ID {coach_id} was found."
        return f"Coach ID {coach_id} updated successfully!"
#print(update_coach(13, "toto"))

def registrations(id_member, id_course):
   
    with Session(engine) as session:
        
        #recupère tous les id, comme ça le choix
        courses = [course for course in session.exec(select(Courses.course_id)).all()]
        #récupérer le time plan associé à un id
        statement_time = select(Courses.time_plan).where(Courses.course_id==id_course)
        time_plan= session.exec(statement_time).one()
        # Récupérer le nombre actuel de participants pour chaque cours
        statement = (
            select(Registrations.course_id, func.count(Registrations.member_id).label('nb_participants'))
            .group_by(Registrations.course_id)
        )
        course_participants = {
            row.course_id: row.nb_participants for row in session.exec(statement).all()
        }

        # Ajouter les cours sans inscription dans le dictionnaire
        for course_id in courses:
            if course_id not in course_participants:
                course_participants[course_id] = 0

        if course_id in courses:
            # Filtrer les cours disponibles (moins de 10 participants)
            available_courses = [course_id for course_id, count in course_participants.items() if count < 10]

            if not available_courses:
                raise ValueError('All course are fulled')
              

            # Créer une nouvelle inscription
            new_registration = Registrations(
                registration_date=time_plan,
                member_id=id_member,
                course_id=id_course
            )

            session.add(new_registration)

            try:

                session.commit()
       
            except IntegrityError:
                # Si un doublon est détecté, ignorer cette tentative
                session.rollback()
               
            v=(f"Member {id_member} succesfully registered ")
        return v
    

#print(registrations(4,9))