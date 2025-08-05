# config.py
import streamlit as st
MONGO_URI = st.secrets["MONGO_URI"]
DB_NAME = "student_db"
COLLECTION_NAME = "questionnaires"


