from sqlalchemy.exc import IntegrityError, NoResultFound, SQLAlchemyError
from faker import Faker
from sqlmodel import Session, select, func, delete, and_, update
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


def add_course(name:str, date:str, max_participants:int, coach_Id:int)->str:
    """_summary_ addition of a new course

    Args:
        name (str): _description_ name of the specialty of the course
        date (str): _description_ date in a format str
        max_participants (int): _description_ 
        coach_Id (int): _description_ 

    Returns:
        str: _description_ validation message
    """
    session=Session(engine)
    date=datetime.datetime.fromisoformat(date)
    new_course=Courses(course_name=name,
                       time_plan=date,
                       max_capacity=max_participants,
                       coach_id=coach_Id)
    session.add(new_course)
    session.commit()
    validation = f"Addition of the course {name} at {date} with the coach {coach_Id}"
    return validation
#print(add_course("yoga", "2024-11-26 09:00", 10, 3))


def delete_member(name:str) -> str:
    """_summary_delete an existing member from its name

    Args:
        name (str): _description_ name of an existing member

    Returns:
        str: _description_ validation message
    """
    with Session(engine) as session:
        statement= select(Members).where(Members.member_name==name)
        results=session.exec(statement)
        to_delete=results.one()
        session.delete(to_delete)
        session.commit()
        validation=f"The member {name} has been removed from the database"
    return validation
#print(delete_member('Holly Thompson'))


def delete_course(number:int)-> str:
    """_summary_ delete an existing course from a given course_id

    Args:
        number (int): _description_ id_course of a course

    Returns:
        str: _description_ validation message
    """
    with Session(engine) as session:
        statement= select(Courses).where(Courses.course_id==number)
        results=session.exec(statement)
        to_delete=results.one()
        session.delete(to_delete)
        session.commit()
        validation=f"The course {number} has been removed from the database"
    return validation
#print(delete_course(2))
    

def update_members(member_id:int, new_name:str=None, new_mail:str=None)->str:
    """_summary_ allow to modify existing members.

    Args:
        member_id (int): _description_ id of an existing member
        new_name (str, optional): _description_. Defaults to None. 
        new_mail (str, optional): _description_. Defaults to None.

    Returns:
        str: _description_ validation message
    """
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
    validation = f"Member ID {member_id} updated successfully!"
    return validation
#print(update_members(20, "Ludivine"))


def registrations(id_member:int, id_course:int)->str:
    """_summary_ function to create registration to a course with a member_id and a course_id

    Args:
        id_member (int): _description_ 
        id_course (int): _description_

    Raises:
        ValueError: _description_ Can not add a registration to a course if the number of participants is greater than the capacity

    Returns:
        str: _description_ validation message
    """
    with Session(engine) as session:
        #get all the courses_id
        courses = [course for course in session.exec(select(Courses.course_id)).all()]
        #get the time plan associated with the id_course
        statement_time = select(Courses.time_plan).where(Courses.course_id==id_course)
        time_plan= session.exec(statement_time).one()
        # get the actual number of participants per course
        statement = (
            select(Registrations.course_id, func.count(Registrations.member_id).label('nb_participants'))
            .group_by(Registrations.course_id)
        )
        course_participants = {
            row.course_id: row.nb_participants for row in session.exec(statement).all()
        }
        # addition of the courses without any participants in the course
        for course_id in courses:
            if course_id not in course_participants:
                course_participants[course_id] = 0

        # Filter courses with less than  participants
        if course_id in courses:
            available_courses = [course_id for course_id, count in course_participants.items() if count < 10]
            #raise error if course is full
            if not available_courses:
                raise ValueError('All course are full')
            
            # Create a new registrations
            new_registration = Registrations(
                registration_date=time_plan,
                member_id=id_member,
                course_id=id_course
            )
            session.add(new_registration)
            try:
                session.commit()
            except IntegrityError:
                # prevent the double registrations
                session.rollback()
            v=(f"Member {id_member} succesfully registered ")
        return v
    

def historic_number_registrations(name:str)->int:
    """_summary_ Return a count of registrations for a given member (name)

    Args:
        name (str): _description_ name of the member, should be the same that the creation of the member

    Returns:
        int: _description_ return the number of inscription
    """
    with Session(engine) as session:
        statement=(select(Members.member_id).where(Members.member_name==name))
        name_id =session.exec(statement).first()
        statementh = select(func.count(Registrations.registration_id)).where(Registrations.member_id == name_id)
        result = session.exec(statementh).one()  # Obtenir une valeur scalaire
    return result
#print(historic_number_registrations("Jessica Price MD"))


def historic_registrations(name:str):
    """_summary_ function to register and show all the registrations for a given member(name)
    Args:
        name (str): _description_ name of the member, should be the same that the creation of the member

    Returns:
        _type_: _description_ list of object registrations for the member
    """
    with Session(engine) as session:
        statement=(select(Members.member_id).where(Members.member_name==name))
        name_id =session.exec(statement).first()
        statementh = select(Registrations).where(Registrations.member_id == name_id)
        result = session.exec(statementh).all()  
    return result
#print(historic_registrations("Jessica Price MD"))