# info.py

# ------------------- Profile -------------------
profile_picture = "nishant_reddy_karri_WebDevLab01/images/spiderman.jpg"
about_me = "I'm Spider-Man. I swing through the city, fight villains, and protect the people of New York."

# Social link icons
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url   = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url    = "https://logowik.com/content/uploads/images/513_email.jpg"

# Social links
my_linkedin_url = "https://www.linkedin.com/in/spiderman-44b857281/"
my_github_url = "https://github.com/nishantkarri"
my_email_address = "spiderman@gmail.com"


# ------------------- Education -------------------
education_data = {
    "Degree": "Bachelor of Science in Computer Science",
    "Institution": "Georgia Institute of Technology",
    "Location": "Atlanta, GA",
    "Graduation Date": "Never",
    "GPA": "4.0",
}

course_data = {
    "code": ["CS 1301", "CS 1332", "MATH 1554", "CS 2050"],
    "names": [
        "Intro to Computing",
        "Data Structures & Algorithms",
        "Linear Algebra",
        "Discrete Mathematics",
    ],
    "semester_taken": ["2nd", "3rd", "2nd", "2nd"],
    "skills": [
        "Developed fundamental programming skills in Python",
        "Implemented core data structures and algorithmic problem-solving in Java",
        "Applied matrix methods to solve systems of equations and transformations",
        "Strengthened logical reasoning through proofs, sets, and combinatorics",
    ],
}


# ------------------- Experience -------------------
experience_data = {
    "Freelance Photographer at Daily Bugle": (
        [
            "- Captured action shots of Spider-Man in the city",
            "- Helped boost newspaper sales with exclusive photos",
            "- Balanced work while hiding my secret identity",
        ],
        "nishant_reddy_karri_WebDevLab01/images/photographer.jpg",
    ),
    "Neighborhood Protector": (
        [
            "- Patrolled the streets of New York to keep citizens safe",
            "- Foiled multiple crimes and supervillain plots",
            "- Built trust as the Friendly Neighborhood Spider-Man",
        ],
        "nishant_reddy_karri_WebDevLab01/images/protector.jpg",
    ),
    "Avengers Team Member": (
        [
            "- Assisted Earth’s Mightiest Heroes in high-stakes battles",
            "- Coordinated with allies like Iron Man and Captain America",
            "- Helped defend New York (and sometimes the galaxy)",
        ],
        "nishant_reddy_karri_WebDevLab01/images/avengers.jpg",
    ),
}


# ------------------- Projects -------------------
projects_data = {
    "Web Shooter Prototype": "Designed and built custom web shooters for mobility and combat",
}


# ------------------- Skills -------------------
programming_data = {
    "Python": 90,
    "Java": 70,
    "C": 40,
    "JavaScript": 80,
    "HTML/CSS": 75,
    "SQL": 65,
    "Rust": 30,
}

programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "C": "🕸️",
    "JavaScript": "⚡",
    "HTML/CSS": "🌐",
    "SQL": "💾",
    "Rust": "🦀",
}

spoken_icons = {
    "English": "🇬🇧",
    "Spanish": "🇪🇸",
    "Italian": "🇮🇹",
}

spoken_data = {
    "English": "Fluent",
    "Spanish": "Conversational",
    "Italian": "Basic",
}


# ------------------- Activities -------------------
leadership_data = {
    "Avengers Initiative": (
        ["- Collaborated with Iron Man, Captain America, and others to save the world"],
        "nishant_reddy_karri_WebDevLab01/images/avengers.jpg",
    ),
}

activity_data = {
    "Friendly Neighborhood Club": [
        "- Helped local citizens with everyday problems",
        "- Balanced hero work with high school life",
    ]
}


# ------------------- Homepage -------------------
homepage_banner = "nishant_reddy_karri_WebDevLab01/images/homepage.jpg"


# ------------------- NBA Quiz -------------------
quiz_result_images = {
    "Scorer": "nishant_reddy_karri_WebDevLab01/images/nba_scorer.jpg",
    "Playmaker": "nishant_reddy_karri_WebDevLab01/images/nba_playmaker.jpg",
    "Defender": "nishant_reddy_karri_WebDevLab01/images/nba_defender.jpg",
    "Sharpshooter": "nishant_reddy_karri_WebDevLab01/images/nba_sharpshooter.jpg",
    "All-Around": "nishant_reddy_karri_WebDevLab01/images/nba_allaround.jpg",
    "Interior Force": "nishant_reddy_karri_WebDevLab01/images/nba_interiorforce.jpg",
}

quiz_archetype_icons = {
    "Scorer": "🎯",
    "Playmaker": "🧩",
    "Defender": "🛡️",
    "Sharpshooter": "🎯🔫",
    "All-Around": "🦁",
    "Interior Force": "🦍",
}

quiz_questions = {
    "q1": {
        "text": "Q1. What’s your go-to move? 🤔",
        "options": [
            "Blow-by drive to the rim 🏃‍♂️💨",
            "No-look dime 👀➡️",
            "Lockdown on-ball defense 🛡️",
            "Catch-and-shoot three 🎯🏀",
            "Barrel into the paint 💪🏀",
            "Do a little bit of everything 🦁",
        ],
    },
    "q2": {
        "text": "Q2. Pick your top TWO strengths 💪",
        "options": [
            "Shot creation 🎨",
            "Court vision 👓",
            "Perimeter defense 🚧",
            "Shooting range 📏🏀",
            "Dominating inside 🦍",
            "Versatility 🦁",
        ],
    },
    "q3": {
        "text": "Q3. How confident are you taking the last shot? ⏰🏀",
        "min": 0,
        "max": 10,
        "default": 5,
    },
    "q4": {
        "text": "Q4. What’s your height in inches? 📏 (e.g., 72 for 6'0\")",
        "min": 55,
        "max": 90,
        "default": 72,
        "step": 1,
    },
    "q5": {
        "text": "Q5. Pick the legend you study the most 🌟",
        "options": [
            "Michael Jordan 🐐",
            "Chris Paul 🎮",
            "Kawhi Leonard 🤐",
            "Stephen Curry 🎯",
            "LeBron James 👑",
            "Shaquille O’Neal 🦍",
        ],
    },
    "q6": {
        "text": "Q6. Weekly solo shooting reps (in hundreds) 🔄🏀",
        "min": 0,
        "max": 20,
        "default": 5,
    },
}

quiz_legend_map = {
    "Michael Jordan 🐐": "Scorer",
    "Chris Paul 🎮": "Playmaker",
    "Kawhi Leonard 🤐": "Defender",
    "Stephen Curry 🎯": "Sharpshooter",
    "LeBron James 👑": "All-Around",
    "Shaquille O’Neal 🦍": "Interior Force",
}
