from sqlalchemy.exc import IntegrityError, NoResultFound, SQLAlchemyError
from faker import Faker
from sqlmodel import Session, select, func, delete, and_, update
from sqlmodel import Session, select, func, delete
from model import Members, Coaches, Accesscards, Registrations, Courses
from init_db import engine
import datetime
import pandas as pd


def all_coach_info():
    """Retrieve all coach information from the database."""
    try:
        with Session(engine) as session:
            stmt = select(Coaches)
            results = session.exec(stmt).all()
            data = [{"coach_id": row.coach_id, "coach_name": row.coach_name, "specialty": row.specialty} for row in results]
            df = pd.DataFrame(data)
            df.index = df.index + 1  # Start index from 1
            return df
    except SQLAlchemyError as e:
        print(f"Database error in all_coach_info(): {e}")
        return pd.DataFrame()  # Return an empty DataFrame if there is an error


def add_coach(name, specialty):
    """Add a new coach to the database with the specified name and specialty."""
    try:
        with Session(engine) as session:
            new_coach = Coaches(coach_name=name, specialty=specialty)
            session.add(new_coach)
            session.commit()
            print(f"Successfully added coach {name}")
            return True, f"Addition of the new coach {name} successful"
    except SQLAlchemyError as e:
        print(f"Error adding coach {name}: {e}")
        return False, f"Error adding coach {name}: {e}"

def delete_coach(coach_id):
    """Delete a coach from the database by their unique ID."""
    try:
        with Session(engine) as session:
            statement = select(Coaches).where(Coaches.coach_id == coach_id)
            to_delete = session.exec(statement).one_or_none()
            if not to_delete:
                print(f"No coach found with ID: {coach_id}")
                return False, f"No coach found with ID: {coach_id}"
            session.delete(to_delete)
            session.commit()
            print(f"Successfully deleted coach with ID: {coach_id}")
            return True, f"Coach with ID: {coach_id} deleted successfully"
    except SQLAlchemyError as e:
        print(f"Error deleting coach with ID {coach_id}: {e}")
        return False, f"Error deleting coach: {e}"

from sqlalchemy.exc import SQLAlchemyError

def modify_coach(coach_id, new_name=None, new_specialty=None):
    try:
        with Session(engine) as session:
            # Retrieve the coach to modify
            statement = select(Coaches).where(Coaches.coach_id == coach_id)
            coach_to_modify = session.exec(statement).one_or_none()

            if not coach_to_modify:
                return False, f"No coach found with ID: {coach_id}"

            # Update the coach's name and specialty if new values are provided
            if new_name:
                coach_to_modify.coach_name = new_name
            if new_specialty:
                coach_to_modify.specialty = new_specialty

            # Commit the changes
            session.commit()
            print(f"Successfully modified coach with ID: {coach_id}")
            return True, f"Coach with ID: {coach_id} updated successfully"
    except SQLAlchemyError as e:
        print(f"Error modifying coach with ID {coach_id}: {e}")
        return False, f"Error modifying coach: {e}"


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

    return f"Addition of the new member {name}"
#print(add_member("toto", "toto@mail", 123456))


def add_coache(name, spe):
def add_course(name, date, max_participants, coach_Id):
    session=Session(engine)
    new_coache=Coaches(coach_name=name, 
                        specialty=spe)
    session.add(new_coache)
    date=datetime.datetime.fromisoformat(date)
    new_course=Courses(course_name=name,
                       time_plan=date,
                       max_capacity=max_participants,
                       coach_id=coach_Id)
    session.add(new_course)
    session.commit()
    return f"Addition of the course {name} at {date} with the coach {coach_Id}"

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

def historic_registrations(name):
    with Session(engine) as session:
        statement=(select(Members.member_id).where(Members.member_name==name))
        name_id =session.exec(statement).all()
        statementh = (select(func.count(Registrations.registration_id)).where(Registrations.member_id==name_id))
        result=statementh
        return result

#print(historic_registrations("Jessica Price MD"))
    
