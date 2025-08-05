# utils.py

import streamlit as st
import re

def student_information():
    st.subheader("👤 Student Information")
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    grade = st.selectbox("Grade", options=["", "6", "7", "8", "9", "10", "11", "12"])
    section = st.text_input("Section (e.g., A, B, C)")

    errors = []

    if email and not email.endswith("@indusschool.com"):
        errors.append("Email must end with @indusschool.com")

    if section and not re.fullmatch(r"[A-Za-z]", section):
        errors.append("Section must be a single alphabet letter (A-Z or a-z)")

    if errors:
        for error in errors:
            st.error(error)

    return {
        "full_name": full_name,
        "email": email,
        "grade": grade,
        "section": section,
        "is_valid": not errors
    }

def learning_preferences():
    st.subheader("📘 A little about you...")
    learning_style = st.radio("When learning something new, I prefer to:",
        options=["A) Watch a video or see a diagram", 
                 "B) Listen to someone explain it", 
                 "C) Try it myself and learn by doing"])
    
    memory = st.radio("If I forget something, I usually:",
        options=["A) Picture it in my mind", 
                 "B) Say it out loud or hear it in my head", 
                 "C) Remember how I felt doing it"])
    
    comprehension = st.radio("I understand a topic best when I:",
        options=["A) Use charts, maps, or pictures", 
                 "B) Talk about it or hear a lecture", 
                 "C) Build, move, or experiment with it"])
    
    class_pref = st.radio("In class, I prefer:",
        options=["A) Slides, notes, or drawing", 
                 "B) Class discussions or group talks", 
                 "C) Hands-on activities or labs"])
    
    study_style = st.radio("When studying, I like to:",
        options=["A) Highlight or make visual notes", 
                 "B) Read out loud or record notes", 
                 "C) Walk around, act it out, or use flashcards"])
    
    return {
        "learning_style": learning_style,
        "memory": memory,
        "comprehension": comprehension,
        "class_preference": class_pref,
        "study_style": study_style
    }

def hobbies_interests():
    st.subheader("🎨 Hobbies & Interests")

    free_time = st.multiselect(
        "What do you love doing in your free time?",
        options=["Drawing", "Reading", "Playing Sports", "Gaming", "Music", "Others"]
    )

    other_hobby = st.text_input("Other hobby (optional)")
    fav_activity = st.text_input("What's one hobby or activity you never get bored of?")

    project_type = st.radio("What kind of school projects do you enjoy the most?",
        options=["A) Creative ones like posters, videos, or art",
                 "B) Talking or presenting in front of others",
                 "C) Experiments, building models, or group work"])
    
    return {
        "free_time_hobbies": free_time,
        "other_hobby": other_hobby,
        "favorite_activity": fav_activity,
        "project_type": project_type
    }
