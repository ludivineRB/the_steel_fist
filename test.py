import streamlit as st
from init_db import engine
from sqlmodel import Session, select, func
from model import Members, Coaches, Accesscards, Registrations, Courses
from utils import add_member, add_coaches, select_course
import pandas as pd

def coach_list(refresh=False):
    with Session(engine) as session:
        # Join query between Coaches and Courses
        stmt = select(Coaches, Courses).join(Courses, Coaches.coach_id == Courses.coach_id)
        results = session.exec(stmt).all()

        # Convert each row to a dictionary with keys from both Coaches and Courses
        data = [
            {**row.Coaches.__dict__, **row.Courses.__dict__}
            for row in results
        ]

        # Clean up dictionary entries (remove private SQLAlchemy fields like _sa_instance_state)
        for entry in data:
            entry.pop('_sa_instance_state', None)

        # Create DataFrame
        df = pd.DataFrame(data)
        df.index = df.index + 1
        return df