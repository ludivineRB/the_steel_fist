import streamlit as st
import sqlite3
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from admin_auth import authentify_admin_login

authentication_status=authentify_admin_login()[0]
st.session_state["authentication_status"] = authentication_status
if authentication_status:
    print("True")
else: 

# if "authentication_status" not in st.session_state or not st.session_state["authentification_status"]:
#     st.session_state["authentication_status"] = authentication_status

# # logout=authentify_admin_login()[1]

#     #st.session_state["authentication_status"] = authentification_status

# if st.session_state["authentication_status"] == False:
#     st.error("Username or Password is invalid. Try again")

# elif st.session_state["authentication_status"] is None:
#     st.error("Please enter your username and Password")

# elif st.session_state["authentication_status"] == True:

#             st.title("The Steel Fist")

#             #st.write(f'Welcome to control center *{st.session_state["name"]}*')

#             page = st.sidebar.selectbox("pages", ["Register new member", "View client list"])

#             if page == "Register new member":
#                 st.write(f'Welcome *{st.session_state["name"]}*, add new members to database here')
            
#             elif page == "View client list":
#                 #logout
#                 st.write(f'Hi *{st.session_state["name"]}*, review registered members here')
#                 st.title("The Steel Fist")
                

    
