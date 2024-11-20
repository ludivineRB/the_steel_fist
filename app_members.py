import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('xxxx.db')
cursor = conn.cursor()

st.title("The Steel Fist Company")
