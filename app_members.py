import streamlit as st
import datetime

st.title("Registration")

if 'stage' not in st.session_state:
    st.session_state.stage = 0
    
progress_text = f"Stage {st.session_state.stage + 1} of 5"
progress_value = (st.session_state.stage + 1) / 5
st.progress(progress_value, text=progress_text)


def process_form():
    st.session_state.form_submitted = True

if 'stage' not in st.session_state:
    st.session_state.stage = 0

if st.session_state.stage == 0:
    with st.form("personal_details", enter_to_submit=False):
        st.header("Personal Details")
        name = st.text_input("Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", placeholder="Create password", type="password")

        submitted = st.form_submit_button("Next", on_click=process_form)

    if st.session_state.get('form_submitted', False):
        if name and email and password:
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.password = password
            st.session_state.stage = 1
            st.session_state.form_submitted = False
            st.rerun()
        else:
            st.error("Please fill in all fields.")
            st.session_state.form_submitted = False

elif st.session_state.stage == 1:
    with st.form("choose_program"):
        st.header("Choose Program")
        program_options = ["Zumba", "Crossfit", "Body Training", "Yoga", "Athletes Training", "Pilates", "Calisthenic"]
        selected_program = st.selectbox("Choose program", program_options)
        submitted = st.form_submit_button("Next", on_click=process_form)

    if st.session_state.get('form_submitted', False):
        if selected_program:
            st.session_state.selected_program = selected_program
            st.session_state.stage = 2
            st.session_state.form_submitted = False
            st.rerun()
        else:
            st.error("Please select a program.")
            st.session_state.form_submitted = False

elif st.session_state.stage == 2:
    with st.form("choose_date"):
        st.header("Choose Date")
        date = st.date_input("Select a date", min_value=datetime.date.today())
        submitted = st.form_submit_button("Next", on_click=process_form)

    if st.session_state.get('form_submitted', False):
        if date:
            st.session_state.selected_date = date
            st.session_state.stage = 3
            st.session_state.form_submitted = False
            st.rerun()
        else:
            st.error("Please select a date.")
            st.session_state.form_submitted = False

elif st.session_state.stage == 3:
    with st.form("choose_time"):
        st.header("Choose Time")
        time = st.time_input("Select a time")
        submitted = st.form_submit_button("Next", on_click=process_form)

    if st.session_state.get('form_submitted', False):
        if time:
            st.session_state.selected_time = time
            st.session_state.stage = 4
            st.session_state.form_submitted = False
            st.rerun()
        else:
            st.error("Please select a time.")
            st.session_state.form_submitted = False

elif st.session_state.stage == 4:
    st.header("Review submissions")
    st.write(f"Name: {st.session_state.get('name')}")
    st.write(f"Email: {st.session_state.get('email')}")
    st.write(f"Program: {st.session_state.get('selected_program')}")
    st.write(f"Date: {st.session_state.get('selected_date')}")
    st.write(f"Time: {st.session_state.get('selected_time')}")
    
    if st.button("Submit"):
        # *** Add details to database ***
        st.success("Registration Complete! You can now logout")
        #st.session_state.clear()
        st.session_state.stage = 0

if st.session_state.stage > 0 and st.button("Back"):
    st.session_state.stage -= 1

    # Clear data associated with the current stage
    if st.session_state.stage == 0:
        st.session_state.pop('name', None)
        st.session_state.pop('email', None)
        st.session_state.pop('password', None)
    elif st.session_state.stage == 1:
        st.session_state.pop('selected_program', None)
    elif st.session_state.stage == 2:
        st.session_state.pop('selected_date', None)
    elif st.session_state.stage == 3:
        st.session_state.pop('selected_time', None)
    st.rerun()


# selected_date = st.date_input("Select a date", datetime.date.today())
# selected_time = st.time_input("Select a time", datetime.time(12, 0))

# #available_time_options = [""]

# st.selectbox("Select program", program_options)
# #st.selectbox("Select time schedule", available_time_options)

