import streamlit as st
import info

# Page setup
st.set_page_config(page_title="NBA BuzzFeed Quiz", page_icon="🏀", layout="wide")
st.title("Which NBA Player Archetype Are You? 🏀")
st.caption("Answer the questions below to discover your hoop persona!")

# Use centralized data
RESULT_IMAGES = info.quiz_result_images
ARCHETYPE_ICONS = info.quiz_archetype_icons

# Question 1
q1 = st.radio(
    info.quiz_questions["q1"]["text"],
    options=info.quiz_questions["q1"]["options"]
)

# Question 2
q2 = st.multiselect(
    info.quiz_questions["q2"]["text"],
    options=info.quiz_questions["q2"]["options"],
    default=[]
)

# Question 3
q3 = st.slider(
    info.quiz_questions["q3"]["text"],
    min_value=info.quiz_questions["q3"]["min"],
    max_value=info.quiz_questions["q3"]["max"],
    value=info.quiz_questions["q3"]["default"]
)

# Question 4
q4 = st.number_input(
    info.quiz_questions["q4"]["text"],
    min_value=info.quiz_questions["q4"]["min"],
    max_value=info.quiz_questions["q4"]["max"],
    value=info.quiz_questions["q4"]["default"],
    step=info.quiz_questions["q4"]["step"]
)

# Question 5
q5 = st.selectbox(
    info.quiz_questions["q5"]["text"],
    options=info.quiz_questions["q5"]["options"]
)

# Question 6
q6 = st.slider(
    info.quiz_questions["q6"]["text"],
    min_value=info.quiz_questions["q6"]["min"],
    max_value=info.quiz_questions["q6"]["max"],
    value=info.quiz_questions["q6"]["default"]
)

# Initialize scores
scores = {
    "Scorer": 0,
    "Playmaker": 0,
    "Defender": 0,
    "Sharpshooter": 0,
    "All-Around": 0,
    "Interior Force": 0,
}

# Map Q1 answers
if "drive" in q1:
    scores["Scorer"] += 2
elif "dime" in q1:
    scores["Playmaker"] += 2
elif "defense" in q1:
    scores["Defender"] += 2
elif "three" in q1:
    scores["Sharpshooter"] += 2
elif "paint" in q1:
    scores["Interior Force"] += 2
elif "everything" in q1:
    scores["All-Around"] += 2

# Map Q2 answers
for choice in q2:
    if "Shot creation" in choice:
        scores["Scorer"] += 1
    elif "Court vision" in choice:
        scores["Playmaker"] += 1
    elif "Perimeter defense" in choice:
        scores["Defender"] += 1
    elif "Shooting range" in choice:
        scores["Sharpshooter"] += 1
    elif "inside" in choice:
        scores["Interior Force"] += 1
    elif "Versatility" in choice:
        scores["All-Around"] += 1

# Map Q3 answers
if q3 >= 8:
    scores["Scorer"] += 2
    scores["All-Around"] += 1
elif q3 >= 5:
    scores["Scorer"] += 1
    scores["Sharpshooter"] += 1
else:
    scores["Playmaker"] += 1

# Map Q4 answers
if q4 >= 80:
    scores["Defender"] += 2
    scores["Interior Force"] += 1
elif q4 >= 74:
    scores["Scorer"] += 1
    scores["Defender"] += 1
elif q4 <= 70:
    scores["Playmaker"] += 1
    scores["Sharpshooter"] += 1
    scores["All-Around"] += 1

# Map Q5 answers
scores[info.quiz_legend_map[q5]] += 2

# Map Q6 answers
if q6 >= 12:
    scores["Sharpshooter"] += 2
elif q6 >= 6:
    scores["Sharpshooter"] += 1
    scores["Scorer"] += 1
else:
    scores["Playmaker"] += 1
    scores["All-Around"] += 1

# Show running tally
st.write("### Current Tally 📊")
for role, pts in scores.items():
    st.write(f"{ARCHETYPE_ICONS[role]} **{role}**: {pts} pts")

# Reveal result
if st.button("Reveal My Archetype 🚀"):
    winner = max(scores, key=scores.get)
    st.success(f"You are: {ARCHETYPE_ICONS[winner]} **{winner}**")
    img_path = RESULT_IMAGES.get(winner)
    if img_path:
        st.image(img_path, caption=f"{winner} {ARCHETYPE_ICONS[winner]}", use_container_width=True)
    st.balloons()
