import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/resume_model.pkl")

st.title("AI-Based Resume Screening System")

st.write("Enter candidate details to predict whether the candidate will be shortlisted.")

years_experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=50,
    value=2
)

skills_match_score = st.number_input(
    "Skills Match Score",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

education_level = st.selectbox(
    "Education Level",
    ["High School", "Bachelors", "Masters", "PhD"]
)

project_count = st.number_input(
    "Number of Projects",
    min_value=0,
    max_value=100,
    value=5
)

resume_length = st.number_input(
    "Resume Length",
    min_value=0,
    max_value=2000,
    value=500
)

github_activity = st.number_input(
    "GitHub Activity",
    min_value=0,
    max_value=2000,
    value=200
)

if st.button("Screen Candidate"):

    candidate = pd.DataFrame({
        "years_experience": [years_experience],
        "skills_match_score": [skills_match_score],
        "education_level": [education_level],
        "project_count": [project_count],
        "resume_length": [resume_length],
        "github_activity": [github_activity]
    })

    prediction = model.predict(candidate)[0]
    probability = model.predict_proba(candidate)[0][1]

    if prediction == 1:
        st.success("Candidate is Shortlisted")
    else:
        st.error("Candidate is Not Shortlisted")

    st.write(
        f"Shortlisting Probability: {probability * 100:.2f}%"
    )