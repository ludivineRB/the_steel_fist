import streamlit as st
from init_db import engine
from sqlmodel import Session, select, join
from model import Members, Coaches, Accesscards, Registrations, Courses
from utils import add_member, add_coaches, select_course
import pandas as pd

st.header("Manage coaches")

def coach_list():
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
        
        return st.dataframe(df)

if "df" not in st.session_state:
    st.session_state.df = coach_list()

st.write(" What do you want to do?")

col1, col2, col3 = st.columns(3)


with col1:

    if st.button('Add coach'):

        with st.form("coach_form"): 
            st.text_input("Enter coach name")
            specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
            st.selectbox("Choose coach specialty", specialty_list)

            if st.form_submit_button("Add coach to database"):
                ###Update database





# # if "action" not in st.session_state:
# #     st.session_state.action = None

with col1:
    add = st.button("Add coach")
    if add:
        st.text_input("Enter coach name")
        specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
        st.selectbox("Choose coach specialty", specialty_list)

with col2:
    st.button("Modify coach")

with col3:
    st.button("Delete coach")




#         """Login Page"""
#     st.header("Page View")
#     role = st.selectbox("Login as:", ROLES)

#     if st.button("Login"):
#         if role != "—":  # Prevent setting role to "—"
#             st.session_state["role"] = role
#             st.rerun()
#         else:
#             st.warning("Please select a valid role.")
