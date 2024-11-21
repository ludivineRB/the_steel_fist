import streamlit as st

st.header("Course Registration")
st.write("This is the course registration page.")
st.write(f"You are logged in as a {st.session_state["role"]}.")
