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
    




    ################


@st.cache_data
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

def add_coach(name, specialty):
    # Update the database
    with Session(engine) as session:
        new_coach = Coaches(coach_name=name, specialty=specialty)
        session.add(new_coach)
        session.commit()

    # Update the cached dataframe in session state
    new_row = pd.DataFrame({'name': [name], 'specialty': [specialty]})
    st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)

    return f"Addition of the new coach: {name}"

# Initialize session state for df if not already set
if "df" not in st.session_state:
    st.session_state.df = coach_list()

# Display the current list of coaches in a dataframe
st.write("Current List of Coaches:")
st.dataframe(st.session_state.df)

# Create buttons for Add, Modify, and Delete actions
col1, col2, col3 = st.columns(3)
add_button = col1.button("Add Coach")
modify_button = col2.button("Modify Coach")
delete_button = col3.button("Delete Coach")

# Container for the entry form that appears when "Add Coach" is clicked
if add_button:
    with st.container():
        with st.form("add_form"):
            st.write("Enter details for the new coach")
            # Form fields for new coach details
            c_name = st.text_input("Enter coach name")
            specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
            selected_specialty = st.selectbox("Choose coach specialty", specialty_list)
            coach_add = st.form_submit_button("Submit")

        # If the form is submitted, add the new coach to the database and update the dataframe
        if coach_add:
            result = add_coach(c_name, selected_specialty)
            st.success(result)
            
            # Refresh session state with updated database content
            st.session_state.df = coach_list(refresh=True)
            st.write("Updated List of Coaches:")
            st.dataframe(st.session_state.df)

