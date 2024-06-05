from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
css_file2 = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic_path = current_dir / "assets" / "pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Manoj Mahato"
PAGE_ICON = ":wave:"
NAME = "Manoj Mahato"
DESCRIPTION = "SDE"
EMAIL = "manojmahato08779@gmail.com"
SOCIAL_MEDIA = {
    "LeetCode": "https://leetcode.com/u/Fortnight_6969/",
    "LinkedIn": "https://www.linkedin.com/in/manoj-mahato-5531531ba/",
    "GitHub": "https://github.com/Manoj-Mahat0",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Health Horizons - Multiple Disease Prediction using Machine Learning": "https://health-horizon.onrender.com/",
    "🏆 Health Expense Pro - Predict Insurance You Deserve": "https://healthexpensepro.onrender.com/",
    "🏆 Movie Recommendation System - A content-based recommender system that recommends movies": "https://movie-rgq6.onrender.com/",
    "🏆 Scam Detection - Using Sentimental Analysis": "https://scam-o7o7.onrender.com/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(css_file2) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 3 Years experience extracting actionable insights from data
- ✔️ Strong hands-on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visualization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
    """
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Software Quality Tester | 366pi**")
st.write("08/2023 - 10/2023")
st.write(
    """
- ► Design and develop test plans and test cases
- ► Execute manual and automated tests
- ► Continuously improve testing processes and methodologies
    """
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Python Developer | Blackcoffer**")
st.write("03/2024 - 05/2024")
st.write(
    """
- ► Data Scraping: Extracted data from various websites using web scraping techniques to gather large datasets for analysis.
- ► Sentiment Analysis: Employed natural language processing (NLP) tools and algorithms to perform sentiment analysis on the scraped data, identifying and categorizing sentiments expressed in the content.
- ► Insights and Outcomes: Analyzed the sentiment data to derive meaningful insights, helping to inform business decisions or strategies based on the public sentiment trends identified.
    """
)

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.header(":mailbox: Get In Touch With Me!")

contact_form = f"""
<form action="https://formsubmit.co/manojmahato08779@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(css_file2)
