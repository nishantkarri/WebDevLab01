import streamlit as st
import info

st.set_page_config(page_title="Home — Web Dev Lab01", page_icon="🏠", layout="wide")

# ===== Header (required) =====
st.title("Nishant Reddy Karri")
st.subheader("CS 1301 — Web Development Lab 01")

st.write("---")

# Optional banner (offloaded to info.py; safe if missing)
try:
    st.image(info.homepage_banner, use_container_width=True)
except Exception:
    pass

st.write("## Welcome")
st.write(
    "Use the sidebar or the buttons below to navigate between pages. "
    "Here’s what’s included in this app:"
)

# ===== Required page descriptions =====
st.markdown("1. **Portfolio** — Personal profile with education, experience, projects, skills, and activities.")
st.markdown("2. **BuzzFeed-Style NBA Quiz** — Take a fun quiz to find your NBA player archetype.")

st.write("---")

# ===== Quick navigation buttons =====
col1, col2 = st.columns(2)
with col1:
    if st.button("Go to Portfolio 🧑‍💻"):
        st.switch_page("pages/Portfolio.py")
with col2:
    if st.button("Take the NBA Quiz 🏀"):
        st.switch_page("pages/NBA_Quiz.py")

st.caption("Tip: You can also switch pages from the left sidebar at any time.")
