from sqlmodel import SQLModel, Field, create_engine
from datetime import datetime
#from typing import Optional


class Members(SQLModel, table=True):
    member_id: int | None = Field(default=None, primary_key=True, nullable=False)
    member_name: str = Field(index=True, nullable=False)
    email: str = Field(index=True, nullable=False)

    access_card_id: int | None = Field(default=None, foreign_key="accesscards.card_id")

class Accesscards(SQLModel, table=True):
    card_id: int = Field(default=None, primary_key=True, nullable=False)
    unique_number: int 

class Registrations(SQLModel, table=True):
    registration_id: int | None = Field(default=None, primary_key=True)
    registration_date: datetime = Field(nullable=False)

    member_id: str = Field(default=None, foreign_key="members.member_id")
    course_id: str = Field(default=None, foreign_key="courses.course_id")

class Coaches(SQLModel, table=True):
    coach_id: int | None = Field(default=None, primary_key=True)
    coach_name: str = Field(index=True, nullable=False)
    specialty: str

class Courses(SQLModel, table=True):
    course_id: int | None = Field(default=None, primary_key=True, nullable=False)
    course_name: str = Field(index=True, nullable=False)
    time_plan: datetime = Field(index=True, nullable=False)
    max_capacity: int

    coach_id: int | None = Field(default=None, foreign_key="coaches.coach_id")
