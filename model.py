from sqlmodel import SQLModel, Field, Relationship 
from datetime import datetime, date
from typing import Optional


class Members(SQLModel, table=True):
    member_id: int | None = Field(default=None, primary_key=True, nullable=False)
    member_name: str = Field(index=True, nullable=False)
    email: str = Field(index=True, nullable=False)

    access_card_id: int | None = Field(default=None, foreign_key="accesscards.card_id")
    access_card: Optional["Accesscards"] = Relationship(back_populates="member")
    registration: list["Registrations"] = Relationship(back_populates="member")

class Accesscards(SQLModel, table=True):
    card_id: int | None  = Field(default=None, primary_key=True, nullable=False)
    unique_number: int 

    member: Optional["Members"] = Relationship(sa_relationship_kwargs={'uselist': False}, back_populates="access_card")

class Registrations(SQLModel, table=True):
    registration_id: int | None = Field(default=None, primary_key=True)
    registration_date: date = Field(nullable=False)

    member_id: str = Field(default=None, foreign_key="members.member_id")
    course_id: str = Field(default=None, foreign_key="courses.course_id")
    member: Optional["Members"] = Relationship(back_populates="registration")
    course: Optional["Courses"] = Relationship(back_populates="registration")

class Coaches(SQLModel, table=True):
    coach_id: int | None = Field(default=None, primary_key=True)
    coach_name: str = Field(index=True, nullable=False)
    specialty: str

    course: list["Courses"] = Relationship(back_populates="coach")

class Courses(SQLModel, table=True):
    course_id: int | None = Field(default=None, primary_key=True, nullable=False)
    course_name: str = Field(index=True, nullable=False)
    time_plan: datetime = Field(index=True, nullable=False)
    max_capacity: int

    coach_id: int | None = Field(default=None, foreign_key="coaches.coach_id")
    registration: list["Registrations"] = Relationship(back_populates="course")
    coach: Optional["Coaches"] = Relationship(back_populates="course")
