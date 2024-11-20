import streamlit as st

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

# Main app logic
role = st.session_state["role"]

# Create all pages

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("pages/settings.py", title="Settings", icon=":material/settings:")
users_registeration = st.Page("pages/app_members.py", title="Manage courses", icon="👤️",  default=(role == "User"))
manage_coaches = st.Page("pages/manage_coaches.py", title="Manage coaches", icon="🏋️", default=(role == "Admin"))
manage_courses = st.Page("pages/manage_courses.py", title="Manage courses", icon="📚️")
view_registered_users = st.Page("pages/view_registered_users.py", title="View registered users", icon="🗒️")

account_pages = [logout_page, settings]
user_page = [users_registeration]
admin_pages = [manage_coaches, manage_courses, view_registered_users]

# # Example usage
if st.session_state["role"] is None:
    login()
    
elif st.session_state["role"] == "User":

    st.sidebar.title(f"Welcome {st.session_state['role']}")
    if st.sidebar.button("Logout"):
        logout()

    pg = st.navigation([users_registeration])
    pg.run()

    reg_button = st.button("Register")
    if reg_button:

        # Switch page
        st.switch_page("pages/users_course_registeration")


# elif st.session_state["role"] == "Admin":
#     st.sidebar.title(f"Welcome {st.session_state['role']}")   
else:
    if st.sidebar.button("Logout"):
        logout()
    
