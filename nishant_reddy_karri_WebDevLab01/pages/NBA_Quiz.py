import streamlit as st
import info

# Page setup
st.set_page_config(page_title="NBA BuzzFeed Quiz", page_icon="🏀", layout="wide")
st.title("Which NBA Player Archetype Are You? 🏀")
st.caption("Answer the questions below to discover how you hoop!")

# Use centralized assets from info.py
RESULT_IMAGES = info.quiz_result_images
ARCHETYPE_ICONS = info.quiz_archetype_icons


# Images shown with results
RESULT_IMAGES = {
    "Scorer": "Images/nba_scorer.jpg",
    "Playmaker": "Images/nba_playmaker.jpg",
    "Defender": "Images/nba_defender.jpg",
    "Sharpshooter": "Images/nba_sharpshooter.jpg",
    "All-Around": "Images/nba_allaround.jpg",         # LeBron
    "Interior Force": "Images/nba_interiorforce.jpg", # Shaq
}

# Icons for each archetype
ARCHETYPE_ICONS = {
    "Scorer": "🎯",
    "Playmaker": "🧩",
    "Defender": "🛡️",
    "Sharpshooter": "🎯🔫",
    "All-Around": "🦁",       # LeBron
    "Interior Force": "🦍",   # Shaq
}

# -------------------
# Quiz Questions
# -------------------

# Q1 – single choice
q1 = st.radio(
    "Q1. What’s your go-to move? 🤔",
    options=[
        "Blow-by drive to the rim 🏃‍♂️💨",
        "No-look dime 👀➡️",
        "Lockdown on-ball defense 🛡️",
        "Catch-and-shoot three 🎯🏀",
        "Barrel into the paint 💪🏀",
        "Do a little bit of everything 🦁",
    ]
)

# Q2 – multiple select
q2 = st.multiselect(
    "Q2. Pick your top TWO strengths 💪",
    options=[
        "Shot creation 🎨",
        "Court vision 👓",
        "Perimeter defense 🚧",
        "Shooting range 📏🏀",
        "Dominating inside 🦍",
        "Versatility 🦁",
    ],
    default=[]
)

# Q3 – slider
q3 = st.slider(
    "Q3. How confident are you taking the last shot? ⏰🏀",
    min_value=0, max_value=10, value=5
)

# Q4 – number input
q4 = st.number_input(
    "Q4. What’s your height in inches? 📏 (e.g., 72 for 6'0\")",
    min_value=55, max_value=90, value=72, step=1
)

# Q5 – dropdown select
q5 = st.selectbox(
    "Q5. Pick the legend you study the most 🌟",
    options=[
        "Michael Jordan 🐐",
        "Chris Paul 🎮",
        "Kawhi Leonard 🤐",
        "Stephen Curry 🎯",
        "LeBron James 👑",
        "Shaquille O’Neal 🦍",
    ]
)

# Q6 – slider
q6 = st.slider(
    "Q6. Weekly solo shooting reps (in hundreds) 🔄🏀",
    min_value=0, max_value=20, value=5
)

# -------------------
# Scoring system
# -------------------
scores = {
    "Scorer": 0,
    "Playmaker": 0,
    "Defender": 0,
    "Sharpshooter": 0,
    "All-Around": 0,
    "Interior Force": 0,
}

# Q1 mapping
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

# Q2 mapping
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

# Q3 mapping
if q3 >= 8:
    scores["Scorer"] += 2
    scores["All-Around"] += 1
elif q3 >= 5:
    scores["Scorer"] += 1
    scores["Sharpshooter"] += 1
else:
    scores["Playmaker"] += 1

# Q4 mapping
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

# Q5 mapping
legend_map = {
    "Michael Jordan 🐐": "Scorer",
    "Chris Paul 🎮": "Playmaker",
    "Kawhi Leonard 🤐": "Defender",
    "Stephen Curry 🎯": "Sharpshooter",
    "LeBron James 👑": "All-Around",
    "Shaquille O’Neal 🦍": "Interior Force",
}
scores[legend_map[q5]] += 2

# Q6 mapping
if q6 >= 12:
    scores["Sharpshooter"] += 2
elif q6 >= 6:
    scores["Sharpshooter"] += 1
    scores["Scorer"] += 1
else:
    scores["Playmaker"] += 1
    scores["All-Around"] += 1

# -------------------
# Results
# -------------------
st.write("### Current Tally 📊")
for role, pts in scores.items():
    st.write(f"{ARCHETYPE_ICONS[role]} **{role}**: {pts} pts")

if st.button("Reveal My Archetype 🚀"):
    winner = max(scores, key=scores.get)
    st.success(f"You are: {ARCHETYPE_ICONS[winner]} **{winner}**")

    if RESULT_IMAGES.get(winner):
        st.image(
            RESULT_IMAGES[winner],
            caption=f"{winner} {ARCHETYPE_ICONS[winner]}",
            use_container_width=True
        )

    st.balloons()
