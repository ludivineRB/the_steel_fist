import streamlit as st
#from init_db import *
#from sqlmodel import Field, Session, SQLModel, create_engine, select
# import sqlite3
# import pandas as pd
# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader
# from admin_auth import authentify_admin_login


# Initialize session state for role
# if "role" not in st.session_state:
#     st.session_state["role"] = None

# # Debugging session state
# st.write(f"Type of st.session_state: {type(st.session_state)}")
# st.write(f"Content of st.session_state: {st.session_state}")

# # Example usage
# if st.session_state["role"] is None:
#     st.write("No role assigned. Please log in.")
#     if st.button("Set Role to Admin"):
#         st.session_state["role"] = "Admin"
#         st.experimental_rerun()

# st.write(f"Current role: {st.session_state['role']}")

# ROLES = ["—", "User", "Admin"]

# def login():
#     """Login Page"""
#     st.header("Log in")
#     role = st.selectbox("Login as:", ROLES)

#     if st.button("Login"):
#         if role != "—":  # Prevent setting role to "—"
#             st.session_state["role"] = role
#             st.rerun()
#         else:
#             st.warning("Please select a valid role.")

# def logout():
#     """Logout Functionality"""
#     st.session_state["role"] = None
#     st.rerun()

# # Main app logic
# role = st.session_state["role"]

# # Mock Pages
# def settings():
#     st.write("Settings Page")

# def users():
#     st.write("Manage Users Page")

# def manage_coaches():
#     st.write("Manage Coaches Page")

# def manage_courses():
#     st.write("Manage Courses Page")

# def view_registered_users():
#     st.write("View Registered Users Page")

# # Define navigation
# st.title("Account Manager")
# st.image("images/logo.png", width=200)  # Use st.image for displaying logos

# if role is None:
#     login()
# else:
#     st.sidebar.title(f"Welcome, {role}")
#     if st.sidebar.button("Logout"):
#         logout()

#     # Display role-based navigation
#     if role == "User":
#         st.sidebar.write("User Pages")
#         st.sidebar.button("Manage Users", on_click=users)
#     elif role == "Admin":
#         st.sidebar.write("Admin Pages")
#         if st.sidebar.button("Manage Coaches"):
#             manage_coaches()
#         if st.sidebar.button("Manage Courses"):
#             manage_courses()
#         if st.sidebar.button("View Registered Users"):
#             view_registered_users()


# if "role" not in st.session_state:
#     st.session_state["role"] = None

# ROLES = ["—", "User", "Admin"]

# def login():

#     st.header("Log in")
#     role=st.selectbox("Login as:", ROLES)

#     if st.button("Login"):
#         st.session_state["role"] = role
#         st.rerun()

# def logout():
#     st.session_state.role = None
#     st.rerun()

# role = st.session_state["role"]

# logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
# settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
# users = st.Page("app_members.py", title="Manage courses", icon="👤️",  default=(role == "User"))
# manage_coaches = st.Page("manage_coaches.py", title="Manage coaches", icon="🏋️", default=(role == "Admin"))
# manage_courses = st.Page("manage_courses.py", title="Manage courses", icon="📚️")
# view_registered_users = st.Page("view_registered_users.py", title="View registered users", icon="🗒️")

# account_pages = [logout_page, settings]
# user_page = users
# admin_pages = [manage_coaches, manage_courses, view_registered_users]


# st.title("Account manager")

# st.logo("images/name.png", icon_image="images/logo.png")

# page_dict = {}

# if st.session_state.role in ["User", "Admin"]:
#     page_dict["User"] = user_page
# if st.session_state.role == "Admin":
#     page_dict["Admin"] = admin_pages

# if page_dict:
#     pg = st.navigation({"Account": account_pages} | page_dict)
# else:
#     pg = st.navigation([st.Page(login)])

# pg.run()

# st.set_page_config(
#     page_title="Admin center",
#     page_icon="👋",
# )

# st.write("# Welcome to The Steel Fist App Admin Center! 👋")

# page = st.sidebar.selectbox("pages", ["—", "Manage Coaches", "Manage Courses", "View Registered Members"])
# st.sidebar.success("Select a page above.")

# st.markdown(
#     """
#     **👈 Select a page from the sidebar** 
#     ### What you can do on each page:
#     - Manage coaches 
#     - Manage courses 
#     - View the members inscribed for each course per day
# """
# )

# if page == "Manage Coaches":

    # def select_heroes():
    #     with Session(engine) as session:
    #         statement = select(Members)
    #         results = session.exec(statement)
    #         heroes = results.all()
    #         print(heroes)


# if page == "Manage Coaches":

#     st.write('Add new members to database here')

#     name_request = st.text_input("Username")
#     email_request = st.text_input("E-mail")
#     password_request = st.text_input("Password")
    
#     submit =st.button('Submit')

    # if submit:
    #     conn = sqlite3.connect(r'/Users/michaeladebayo/Documents/Simplon/brief_projects/the_steel_fist/steel_fist.db')
    #     cursor = conn.cursor()

        # conn.execute()"INSERT INTO iris () VALUES(xx, xx, xx, xx)",
        # (member_id, xx, xxx, xxx)

        # conn.commit()
        # conn.close()

# else:
#     st.write('Welcome, review registered members here')

    # conn = sqlite3.connect(r'/Users/michaeladebayo/Documents/Simplon/brief_projects/the_steel_fist/steel_fist.db')
    # cursor = conn.cursor()
    # g = cursor.execute('select * from iris')
    # data = g.fetchall()

    # column = [desc[0] for desc in cursor.description]

    # df=pd.DataFrame(data, columns=column)

    # st.dataframe(df)


# if "admin_session" not in st.session_state or not st.session_state["authentication_status"]:
#     authentication_status=authentify_admin_login()
#     st.session_state["authentication_status"] = authentication_status
    
#     if st.session_state["authentication_status"] == False:
#         st.error("Username or Password is invalid. Try again")

#     elif st.session_state["authentication_status"] is None:
#         st.error("Please enter your username and Password")

#     elif st.session_state["authentication_status"] == True:
            
#         st.title("The Steel Fist")

#         st.write(f'Welcome to control center *{st.session_state["name"]}*')

#         page = st.sidebar.selectbox("pages", ["Register new member", "View client list"])
        



    #     st.session_state.clear()


                

    
# if "authentication_status" not in st.session_state:
#     st.session_state["authentication_status"] = None  # Initialize authentication status
#     st.session_state["login_attempted"] = False  # Track if login was attempted

# if not st.session_state["authentication_status"]:
#     authentication_status = authentify_admin_login()
#     st.session_state["authentication_status"] = authentication_status
#     st.session_state["login_attempted"] = True  # Set flag to true after attempting login

#     if st.session_state["authentication_status"] == False:
#         st.error("Username or Password is invalid. Try again")

#     elif st.session_state["authentication_status"] is None and st.session_state["login_attempted"]:
#         st.error("Please enter your username and Password")

#     elif st.session_state["authentication_status"] == True:
#         st.title("The Steel Fist")
#         st.write(f'Welcome to control center *{st.session_state["name"]}*')

#         page = st.sidebar.selectbox("pages", ["Register new member", "View client list"])

#         if page == "Register new member":
#             st.write(f'Welcome *{st.session_state["name"]}*, add new members to database here')

#         elif page == "View client list":
#             st.write(f'Hi *{st.session_state["name"]}*, review registered members here')




    