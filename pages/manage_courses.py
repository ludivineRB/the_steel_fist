import streamlit as st
from init_db import engine
from sqlmodel import Session, select, func
from model import Members, Coaches, Accesscards, Registrations, Courses
from utils import add_course, delete_course
import pandas as pd
import datetime
from datetime import datetime
from streamlit_datetime_range_picker import datetime_range_picker
import streamlit as st
from streamlit_date_picker import date_range_picker, PickerType, date_picker


def courses_list():
    with Session(engine) as session:
        stmt = select(Courses)
        results = session.exec(stmt).all()
        data = [row.__dict__ for row in results]
        for entry in data:
            entry.pop('_sa_instance_state', None)
        df = pd.DataFrame(data)
        #df.index = df.index + 1
        return df
    
def coach_list():
    with Session(engine) as session:
        stmt = select(Coaches)
        results = session.exec(stmt).all()
        data = [row.__dict__ for row in results]
        for entry in data:
            entry.pop('_sa_instance_state', None)
        df2 = pd.DataFrame(data)
        #df.index = df.index + 1
        return df2

    
def date_selector():
    # Sélecteur de date Streamlit
    selected_date = st.text_input("Enter a date (YYYY-MM-DD HH:MM) ")

    return selected_date

# Initialize session state for df if not already set
if "df" not in st.session_state:
    st.session_state.df = courses_list()

# Display the current list of coaches in a dataframe
st.write("Current List of Course:")
st.dataframe(st.session_state.df)

st.write("What do you want to do?")

# Create buttons for Add, Modify, and Delete actions
col1, col2, col3 = st.columns(3)
add_button = col1.button("Add Course")
modify_button = col2.button("Modify Course")
delete_button = col3.button("Delete Course")
# # Check if any button is clicked and display the form accordingly
# if add_button or modify_button or delete_button:
#     with form_container:
#         with st.form("add_form"):

if "add_form_course" not in st.session_state:
    st.session_state.add_form_course = False

if "delete_form_course" not in st.session_state:
    st.session_state.delete_form_course = False

if "modify_form_course" not in st.session_state:
    st.session_state.modify_form_course = False

if add_button:
    st.session_state.add_form_course = True
    st.session_state.delete_form_course = False
    st.session_state.modify_form_course = False

if delete_button:
    st.session_state.delete_form_course = True
    st.session_state.add_form_course = False
    st.session_state.modify_form_course = False

if modify_button:
    st.session_state.delete_form_course = False
    st.session_state.add_form_course = False
    st.session_state.modify_form_course = True


if st.session_state.add_form_course:
    with st.container():
        with st.form("add_form"):
            st.write("Enter details for the new course")
            specialty_list = ["Select", "yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
            selected_specialty = st.selectbox("Choose a course", specialty_list)
            coach_table=coach_list()
            coaches_list = coach_table['coach_id'].tolist()
            coach_id=st.selectbox("Choose a coach", coaches_list)
            date=date_selector()
            max_participants=10
            course_add = st.form_submit_button("Submit")

            # Check if the form is submitted and specialty is valid
            if course_add:
                if selected_specialty != "Select":
                    result = add_course(selected_specialty, date, max_participants,coach_id)
                    st.success(result)
                    st.rerun()

                    # Refresh the dataframe after adding a new coach
                    st.session_state.df = coach_list()
                    st.write("Updated List of Coaches:")
                    st.dataframe(st.session_state.df)
                    st.session_state.add_form_course =False
                else:
                    st.error("Please select a valid specialty.")

if st.session_state.delete_form_course:
    with st.container():
        with st.form("add_form"):
            st.write("Enter details to delete a course")
            courses_table=courses_list()
            courses_id=courses_table['course_id'].tolist()
            course_id = st.selectbox("Choose a course", courses_id)
            course_delete = st.form_submit_button("Submit")
            if course_delete:
                result=delete_course(course_id)
                st.success(result)
                st.rerun()
                st.session_state.df = courses_list()
                st.write("Updated List of Courses:")
                st.dataframe(st.session_state.df)

if st.session_state.modify_form_course:
    with st.container():
        with st.form("add_form"):
            st.write("Enter details to modify a course")
            course_table=courses_list()
            course_id=course_table['course_id'].tolist()
            id_modify = st.selectbox("Choose a course", course_id)
            new_specialty=st.text_input("Enter a new specialty (Optional)", value="")
            date=st.text_input("Enter a new date like YYYY-MM-DD HH:MM (Optional)", value="")

            
            modify_course = st.form_submit_button("Submit")
            if modify_course:
                result=update_course(id_modify,name,mail)
                st.success(result)
                st.rerun()
                st.session_state.df = member_list()
                st.write("Updated List of Members:")
                st.dataframe(st.session_state.df)


#addition of checking of the date before to add a course
#Coach list