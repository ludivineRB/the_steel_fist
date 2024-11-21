import streamlit as st
from init_db import engine
from sqlmodel import Session, select, func
from model import Members, Coaches, Accesscards, Registrations, Courses
from utils import add_member, add_coaches, select_course
import pandas as pd

st.header("Manage coaches")

#@st.cache_data
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

# Initialize session state for df
if "df" not in st.session_state:
    st.session_state.df = coach_list()

st.write("What do you want to do?")

col1, col2, col3 = st.columns(3)

# Create buttons in columns
add_button = col1.button("Add coach")
modify_button = col2.button("Modify coach")
delete_button = col3.button("Delete coach")

form_container = st.container()

# Check if any button is clicked and display the form accordingly
if add_button or modify_button or delete_button:
    with form_container:
        with st.form("add_form"):
            st.write("This form spans the full width of the page")
            # Add your form elements here
            c_name = st.text_input("Enter coach name")
            specialty_list = ["yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
            selected_specialty = st.selectbox("Choose coach specialty", specialty_list)
            
            coach_add = st.form_submit_button("Add coach to database")
        
        if coach_add:
            result = add_coach(c_name, selected_specialty)
            st.success(result)
            
            # Refresh session state with updated database content
            st.session_state.df = coach_list(refresh=True)
            st.write(st.session_state.df)




             

# elif delete_button:
#     with form_container:
#         with st.form("delete_form"):
#             c_name = st.text_input("Enter coach name")
#             list_of_all_coaches = coach_list()
#             list_of_coaches = 






# with col2:
#     st.button("Modify coach")

# with col3:
#     st.button("Delete coach")




#         """Login Page"""
#     st.header("Page View")
#     role = st.selectbox("Login as:", ROLES)

#     if st.button("Login"):
#         if role != "—":  # Prevent setting role to "—"
#             st.session_state["role"] = role
#             st.rerun()
#         else:
#             st.warning("Please select a valid role.")
