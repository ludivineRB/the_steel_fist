import streamlit as st

st.header("View regstered users")
st.write(f"You are logged in as {st.session_state["role"]}.")
