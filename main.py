# main.py

import streamlit as st
from utils import student_information, learning_preferences, hobbies_interests
from database import insert_data

st.set_page_config(page_title="Student Questionnaire", layout="centered")
st.title("📝 Student Questionnaire")

with st.form("student_form"):
    info = student_information()
    prefs = learning_preferences()
    hobbies = hobbies_interests()

    submitted = st.form_submit_button("Submit Questionnaire")

    if submitted:
        if info["is_valid"] and info["full_name"] and info["email"] and info["grade"]:
            info.pop("is_valid")  # Remove validation flag before saving
            data = {**info, **prefs, **hobbies}
            insert_id = insert_data(data)
            st.success(f"✅ Thank you! Your response has been recorded.")
        else:
            st.error("⚠️ Please correct the errors above and ensure all required fields are filled.")
