# sourcery skip: use-named-expression
import streamlit as st
from utils import all_coach_info, add_coach, delete_coach, modify_coach


# Initialize session state for coach list DataFrame if not already set
if "df" not in st.session_state:
    st.session_state.df = all_coach_info()

# Display the current list of coaches in a dataframe
st.write("Current List of Coaches:")
st.dataframe(st.session_state.df)

st.write("What do you want to do?")

# Create buttons for Add, Modify, and Delete actions
col1, col2, col3 = st.columns(3)
add_button = col1.button("Add Coach")
modify_button = col2.button("Modify Coach")
delete_button = col3.button("Delete Coach")

############################################################################

# Manage session state for Add Coach form
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
        with st.form("add_form", clear_on_submit=True):
            st.write("Enter details for the new coach")
            c_name = st.text_input("Enter coach name")
            specialty_list = ["Select", "yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
            selected_specialty = st.selectbox("Choose coach specialty", specialty_list)
            coach_add = st.form_submit_button("Submit")

            if coach_add:
                if selected_specialty != "Select":
                    success, message = add_coach(c_name, selected_specialty)
                    st.write("Add Coach Result:", success, message)  # Debugging output
                    if success:
                        st.success(message)
                        st.session_state.df = all_coach_info()  # Refresh the coach list
                        st.session_state.add_form_coach = False
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.error("Please select a valid specialty.")

#############################################################################

# Manage session state for Delete Coach form
if "delete_form_coach" not in st.session_state:
    st.session_state.delete_form_coach = False
if delete_button:
    st.session_state.delete_form_coach = True

if st.session_state.delete_form_coach:
    coachy = all_coach_info()
    with st.container():
        with st.form("delete_form", clear_on_submit=True):
            list_of_coaches = {f"{coach['coach_name']} (ID: {coach['coach_id']})": coach['coach_id'] for coach in coachy.to_dict(orient='records')}
            selected_coach = st.selectbox("Choose a coach", list(list_of_coaches.keys()))
            del_coach = st.form_submit_button("Approve delete")

            if del_coach:
                coach_id_to_delete = list_of_coaches[selected_coach]
                success, message = delete_coach(coach_id_to_delete)
                st.write("Delete Coach Result:", success, message)  # Debugging output
                if success:
                    st.success(message)
                    st.session_state.df = all_coach_info()  # Refresh the coach list
                    st.session_state.delete_form_coach = False
                    st.rerun()
                else:
                    st.error(message)


#############################################################################

if "modify_form_coach" not in st.session_state:
    st.session_state.modify_form_coach = False

if modify_button:
    st.session_state.modify_form_coach = True

if st.session_state.modify_form_coach:
    current_list = st.session_state.df
    with st.container():
        with st.form("modify_form"):
            coach_to_modify = {f"{coach['coach_name']} (ID: {coach['coach_id']})": coach['coach_id'] for coach in current_list.to_dict(orient='records')}
            selected_coach = st.selectbox("Select coach to modify", list(coach_to_modify.keys()))
            selected_coach_id = st.selectbox(f"Select coach ID (Hint the coach's ID is displayed in front of the coach's name)", list(coach_to_modify.values()))

            if selected_coach and selected_coach_id:
                corected_name = st.text_input("Enter new name", placeholder="Enter the correct name info")
                specialty_list = ["Select", "yoga", "pilates", "crossfit", "calisthenic", "body training", "athletes trainings", "zumba"]
                new_specialty = st.selectbox("Select new program (or select same program assigned)", specialty_list)
                mod_coach = st.form_submit_button("Approve modification")

            if mod_coach:
                if new_specialty != "Select":
                    new_name = corected_name
                    success, message = modify_coach(selected_coach_id, new_name, new_specialty)
                    st.write(f"Updated coach details", success, message)

                if success:
                    st.success(message)
                    st.session_state.df = all_coach_info()  # Refresh the coach list
                    st.session_state.modify_form_coach = False
                    st.rerun()
                else:
                    st.error(message)