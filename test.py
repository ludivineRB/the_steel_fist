import streamlit as st
import datetime

# Initialize session state for role
if "role" not in st.session_state:
    st.session_state["role"] = None

ROLES = ["—", "User", "Admin"]

def login():
    """Login Page"""
    st.header("Page View")
    role = st.selectbox("Login as:", ROLES)

    if st.button("Login"):
        if role != "—":  # Prevent setting role to "—"
            st.session_state["role"] = role
            st.rerun()
        else:
            st.warning("Please select a valid role.")

def logout():
    """Logout Functionality"""
    st.session_state["role"] = None
    st.rerun()

# Main app session state
role = st.session_state["role"]

# Create all pages
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("pages/settings.py", title="Settings", icon=":material/settings:")
main = st.Page("test.py", title="Home")
users_registeration = st.Page("app_members.py", title="User registration", icon="👤️",  default=(role == "User"))
course_register = st.Page("pages/course_registration.py", title="Course registration", icon="📚️")
manage_coaches = st.Page("pages/manage_coaches.py", title="Manage coaches", icon="🏋️", default=(role == "Admin"))
manage_courses = st.Page("pages/manage_courses.py", title="Manage courses", icon="📚️")
view_registered_users = st.Page("pages/view_registered_users.py", title="View registered users", icon="🗒️")

# Group pages by users
account_pages = [logout_page, settings]
user_page = [users_registeration]
admin_pages = [manage_coaches, manage_courses, view_registered_users]

# Navigate pages based on session state status
if st.session_state["role"] is None:
    login()
    
elif st.session_state["role"] == "User":
    
    st.image("images/name1.png", width=200, use_container_width=False)

    st.sidebar.title(f"Welcome {st.session_state['role']}")
    st.sidebar.text(f"You are logged in as a {st.session_state["role"]}.")
    if st.sidebar.button("Logout"):
        st.session_state["login"] = True
        logout()
    
    pg = st.navigation(user_page)
    pg.run()

elif st.session_state["role"] == "Admin":
    st.sidebar.title(f"Welcome {st.session_state['role']}")
    st.sidebar.text(f"You are logged in as an {st.session_state["role"]}.")
    if st.sidebar.button("Logout"):
        logout()

    pg = st.navigation(admin_pages)
    pg.run()
    
