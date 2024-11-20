import streamlit as st

st.header("Register and choose your programs")
st.write(f"You are logged in as a {st.session_state["role"]}.")

st.text_input("Name", placeholder="Enter your name")
st.text_input("Email", placeholder="Enter your e-mail")
st.text_input("Password", placeholder="Create your password")

