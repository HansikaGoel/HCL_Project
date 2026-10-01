import streamlit as st
import pandas as pd
import joblib


# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="ResumeAI",
    page_icon="🤖",
    layout="wide"
)


# =========================
# LOAD MODEL
# =========================

model = joblib.load("models/resume_model.pkl")


# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');


/* ---------- GLOBAL ---------- */

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 8% 10%,
            rgba(124, 58, 237, 0.32),
            transparent 32%
        ),
        radial-gradient(
            circle at 92% 10%,
            rgba(37, 99, 235, 0.28),
            transparent 32%
        ),
        linear-gradient(
            135deg,
            #080d1c 0%,
            #0b1020 50%,
            #071426 100%
        );

    color: white;
}


/* ---------- PAGE SPACING ---------- */

.block-container {
    max-width: 1050px;
    padding-top: 55px !important;
    padding-bottom: 70px !important;
}


/* ---------- TOP BRAND ---------- */

.brand {
    text-align: center;
    color: #c4b5fd;
    font-size: 17px;
    font-weight: 800;
    letter-spacing: 4px;
    margin-bottom: 22px;
}


/* ---------- BADGE ---------- */

.badge {
    width: fit-content;
    margin: 0 auto 25px auto;

    padding: 9px 20px;

    border-radius: 30px;

    background: rgba(124, 58, 237, 0.12);

    border: 1px solid rgba(167, 139, 250, 0.55);

    color: #c4b5fd;

    font-size: 12px;
    font-weight: 700;

    letter-spacing: 1px;

    box-shadow:
        0 0 20px rgba(124, 58, 237, 0.15);
}


/* ---------- HERO TITLE ---------- */

.hero-title {
    text-align: center;

    color: white;

    font-size: 50px;

    font-weight: 800;

    line-height: 1.12;

    margin-top: 10px;

    margin-bottom: 0;
}

.hero-gradient {
    background: linear-gradient(
        90deg,
        #8b5cf6,
        #38bdf8
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}


/* ---------- HERO DESCRIPTION ---------- */

.hero-text {
    max-width: 720px;

    margin: 18px auto 42px auto;

    text-align: center;

    color: #94a3b8;

    font-size: 17px;

    line-height: 1.7;
}


/* =================================================
   CANDIDATE INPUT BOX
================================================= */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background: rgba(10, 17, 34, 0.94) !important;

    border: 2px solid #ffffff !important;

    border-radius: 24px !important;

    padding: 18px 22px 25px 22px !important;

    box-shadow:
        0 0 25px rgba(255, 255, 255, 0.08),
        0 20px 60px rgba(0, 0, 0, 0.40) !important;
}


/* ---------- INPUT TITLE ---------- */

.input-title {
    color: white;

    font-size: 23px;

    font-weight: 700;

    margin-top: 5px;
}


/* ---------- INPUT DESCRIPTION ---------- */

.input-subtitle {
    color: #94a3b8;

    font-size: 14px;

    margin-top: 6px;

    margin-bottom: 25px;
}


/* ---------- LABELS ---------- */

label {
    color: #dbeafe !important;

    font-weight: 600 !important;
}


/* ---------- SELECT BOX ---------- */

div[data-baseweb="select"] > div {

    background-color: #0b1222 !important;

    border: 1px solid #475569 !important;

    border-radius: 10px !important;

    color: white !important;
}


/* ---------- SELECTED TEXT ---------- */

div[data-baseweb="select"] span {

    color: white !important;
}


/* ---------- SLIDERS ---------- */

div[data-testid="stSlider"] {

    padding-bottom: 15px;
}


/* ---------- ANALYZE BUTTON ---------- */

.stButton {
    margin-top: 28px;
}


.stButton > button {

    width: 100%;

    height: 56px;

    border-radius: 13px;

    background: #7c3aed !important;

    color: white !important;

    border: 1px solid #a78bfa !important;

    font-size: 16px !important;

    font-weight: 700 !important;

    box-shadow:
        0 10px 30px rgba(124, 58, 237, 0.35);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        background 0.25s ease;
}


.stButton > button:hover {

    background: #6d28d9 !important;

    color: white !important;

    transform: translateY(-3px);

    box-shadow:
        0 15px 40px rgba(124, 58, 237, 0.50);
}


/* =================================================
   RESULT SECTION
================================================= */

.result-title {

    color: white;

    font-size: 22px;

    font-weight: 700;

    margin-bottom: 10px;
}


/* ---------- SUCCESS MESSAGE ---------- */

div[data-testid="stAlert"] {

    border-radius: 14px !important;

    font-weight: 700 !important;

    border: 1px solid rgba(255, 255, 255, 0.20) !important;
}


/* ---------- METRIC ---------- */

div[data-testid="stMetric"] {

    background: #0b1222;

    border: 1px solid #334155;

    border-radius: 14px;

    padding: 15px;
}


div[data-testid="stMetricLabel"] {

    color: #94a3b8 !important;
}


div[data-testid="stMetricValue"] {

    color: white !important;

    font-weight: 800 !important;
}


/* =================================================
   PROFILE SECTION
================================================= */

.profile-heading {

    color: white;

    font-size: 22px;

    font-weight: 700;

    margin-top: 30px;

    margin-bottom: 15px;
}


/* ---------- PROGRESS ---------- */

div[data-testid="stProgressBar"] {

    margin-top: 10px;
}


/* ---------- FOOTER ---------- */

.footer {

    text-align: center;

    color: #64748b;

    font-size: 13px;

    margin-top: 45px;

    line-height: 1.7;
}


/* =================================================
   ANIMATION
================================================= */

@keyframes fadeUp {

    from {
        opacity: 0;
        transform: translateY(15px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


.result-animation {

    animation: fadeUp 0.5s ease;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HEADER
# =========================

st.markdown(
    '<div class="brand">◈ RESUMEAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="badge">✦ MACHINE LEARNING POWERED</div>',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <div class="hero-title">
        Intelligent Candidate<br>
        <span class="hero-gradient">
            Screening System
        </span>
    </div>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <div class="hero-text">
        Analyze candidate profiles using machine learning and get
        an instant shortlisting prediction based on experience,
        skills, education and activity.
    </div>
    ''',
    unsafe_allow_html=True
)


# =================================================
# CANDIDATE INFORMATION BOX
# =================================================

with st.container(border=True):

    st.markdown(
        '<div class="input-title">👤 Candidate Information</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div class="input-subtitle">
            Enter the candidate details below to begin AI-powered screening.
        </div>
        ''',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)


    # ---------- LEFT COLUMN ----------

    with col1:

        years_experience = st.slider(
            "Years of Experience",
            min_value=0,
            max_value=50,
            value=2
        )

        skills_match_score = st.slider(
            "Skills Match Score",
            min_value=0,
            max_value=100,
            value=70
        )

        education_level = st.selectbox(
            "Education Level",
            [
                "High School",
                "Bachelors",
                "Masters",
                "PhD"
            ]
        )


    # ---------- RIGHT COLUMN ----------

    with col2:

        project_count = st.slider(
            "Number of Projects",
            min_value=0,
            max_value=100,
            value=5
        )

        resume_length = st.slider(
            "Resume Length",
            min_value=0,
            max_value=2000,
            value=500
        )

        github_activity = st.slider(
            "GitHub Activity",
            min_value=0,
            max_value=2000,
            value=200
        )


# =================================================
# ANALYZE BUTTON
# =================================================

screen = st.button(
    "✦  ANALYZE CANDIDATE"
)


# =================================================
# PREDICTION
# =================================================

if screen:

    candidate = pd.DataFrame({

        "years_experience": [
            years_experience
        ],

        "skills_match_score": [
            skills_match_score
        ],

        "education_level": [
            education_level
        ],

        "project_count": [
            project_count
        ],

        "resume_length": [
            resume_length
        ],

        "github_activity": [
            github_activity
        ]
    })


    # ---------- MODEL PREDICTION ----------

    prediction = model.predict(candidate)[0]

    probability = model.predict_proba(candidate)[0][1]

    percentage = probability * 100


    # =================================================
    # RESULT
    # =================================================

    st.markdown(
        '<div class="profile-heading">✦ AI Screening Result</div>',
        unsafe_allow_html=True
    )


    with st.container(border=True):

        if prediction == 1:

            st.success(
                "✓ CANDIDATE SHORTLISTED"
            )

        else:

            st.error(
                "✕ CANDIDATE NOT SHORTLISTED"
            )


        st.metric(
            "Shortlisting Probability",
            f"{percentage:.1f}%"
        )


        st.progress(
            probability,
            text=f"AI Match Confidence: {percentage:.1f}%"
        )


    # =================================================
    # CANDIDATE PROFILE
    # =================================================

    st.markdown(
        '<div class="profile-heading">👤 Candidate Profile</div>',
        unsafe_allow_html=True
    )


    with st.container(border=True):

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Experience",
                f"{years_experience} years"
            )


        with col2:

            st.metric(
                "Skills Match",
                f"{skills_match_score}%"
            )


        with col3:

            st.metric(
                "Education",
                education_level
            )


        col4, col5, col6 = st.columns(3)


        with col4:

            st.metric(
                "Projects",
                project_count
            )


        with col5:

            st.metric(
                "Resume Length",
                resume_length
            )


        with col6:

            st.metric(
                "GitHub Activity",
                github_activity
            )


# =================================================
# FOOTER
# =================================================

st.markdown(
    '''
    <div class="footer">
        ResumeAI · AI-Based Candidate Screening<br>
        Built with Python · Pandas · Scikit-learn · Streamlit
    </div>
    ''',
    unsafe_allow_html=True
)