import streamlit as st
from init_db import engine
from sqlmodel import Session, select, func
from model import Members, Coaches, Accesscards, Registrations, Courses
from utils import add_member, add_coache, select_course, delete_coach
import pandas as pd

def coach_list():
    with Session(engine) as session:
        stmt = select(Coaches)
        results = session.exec(stmt).all()
        data = [row.__dict__ for row in results]
        for entry in data:
            entry.pop('_sa_instance_state', None)
        df = pd.DataFrame(data)
        #df.index = df.index + 1
        return df


# Initialize session state for df if not already set
if "df" not in st.session_state:
    st.session_state.df = coach_list()

# Display the current list of coaches in a dataframe
st.write("Current List of Coaches:")
st.dataframe(st.session_state.df)

st.write("What do you want to do?")

# Create buttons for Add, Modify, and Delete actions
col1, col2, col3 = st.columns(3)
add_button = col1.button("Add Coach")
modify_button = col2.button("Modify Coach")
delete_button = col3.button("Delete Coach")
# # Check if any button is clicked and display the form accordingly
# if add_button or modify_button or delete_button:
#     with form_container:
#         with st.form("add_form"):

if "add_form_coach" not in st.session_state:
    st.session_state.add_form_coach = False

if "delete_form_coach" not in st.session_state:
    st.session_state.delete_form_coach = False

if add_button:
    st.session_state.add_form_coach = True
    st.session_state.delete_form_coach = False

if delete_button:
    st.session_state.add_form_coach = False
    st.session_state.delete_form_coach = True

if st.session_state.add_form_coach:
    with st.container():
        with st.form("add_form"):
            st.write("Enter details for the new coach")
            c_name = st.text_input("Enter coach name")
            specialty_list = ["Select", "yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
            selected_specialty = st.selectbox("Choose coach specialty", specialty_list)
            coach_add = st.form_submit_button("Submit")

            # Check if the form is submitted and specialty is valid
            if coach_add:
                if selected_specialty != "Select":
                    result = add_coache(c_name, selected_specialty)
                    st.success(result)
                    st.rerun()

                    # Refresh the dataframe after adding a new coach
                    st.session_state.df = coach_list()
                    st.write("Updated List of Coaches:")
                    st.dataframe(st.session_state.df)
                else:
                    st.error("Please select a valid specialty.")

if st.session_state.delete_form_coach:
    with st.container():
        with st.form("add_form"):
            st.write("Enter details to delete a coach")
            coach_table=coach_list()
            coaches_list=coach_table['coach_name'].tolist()
            coach = st.selectbox("Choose a coach", coaches_list)
            coach_delete = st.form_submit_button("Submit")
            if coach_delete:
                result=delete_coach(coach)
                st.success(result)
                st.rerun()
                st.session_state.df = coach_list()
                st.write("Updated List of Coaches:")
                st.dataframe(st.session_state.df)

#deletion works only with one row since delete function is built like this. To modify