import streamlit as st
import sqlite3
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from admin_auth import authentify_admin_login
from init_db import *


st.title("The Steel Fist App")
page = st.sidebar.selectbox("pages", ["Register new member", "View client list"])

if page == "Register new member":

    st.write('Add new members to database here')

    name_request = st.text_input("Username")
    email_request = st.text_input("E-mail")
    password_request = st.text_input("Password")
    
    submit =st.button('Submit')

    # if submit:
    #     conn = sqlite3.connect(r'/Users/michaeladebayo/Documents/Simplon/brief_projects/the_steel_fist/steel_fist.db')
    #     cursor = conn.cursor()

        # conn.execute()"INSERT INTO iris () VALUES(xx, xx, xx, xx)",
        # (member_id, xx, xxx, xxx)

        # conn.commit()
        # conn.close()

else:
    st.write('Welcome, review registered members here')

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




    