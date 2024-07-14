import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# PAGE CONFIG

url_icon = "https://raw.githubusercontent.com/M7mdAboBakr/Digital-CV/main/icon.png"
response_icon = requests.get(url_icon)
st.set_page_config(page_title='Digital CV - Mohamed Abobakr', page_icon=Image.open(BytesIO(response_icon.content)))

page_bg_color = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #311c3b;
}}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

    
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Readex+Pro:wght@300;400;500;600;700&display=swap');


* {
    font-family: 'Readex Pro', serif;
}


a {
    text-decoration: none;
    font-weight: 500;
}

a:hover {
    color: #d33682 !important;
    text-decoration: none;
}

ul {list-style-type: none;}

hr {
    margin-top: 0px;
    margin-bottom: 5%;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;} </style>""", unsafe_allow_html=True)

# HEADER SECTION

col1, col2 = st.columns([1, 2], gap="small")

with col1:
    st.markdown("""
      <style>
      .st-emotion-cache-1v0mbdj.e115fcil1 img{
            border-radius: 50%;
      }
      </style>
    """
    , unsafe_allow_html=True)

    url_my_photo = "https://raw.githubusercontent.com/M7mdAboBakr/Digital-CV/main/my_photo.jpg"
    response_my_photo = requests.get(url_my_photo)
    col1.image(Image.open(BytesIO(response_my_photo.content)))
    
    
    

with col2:
    st.markdown(f"""
      <style>
      [class="st-emotion-cache-19rxjzo ef3psqc12"]{{
            background-color: #24162b;’’
      }}
      </style>
    """
    , unsafe_allow_html=True)
    st.title("Mohamed Abobakr")
    st.write("Junior Data Scientist")

    with open("my_resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    col2.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name='my_resume.pdf',
            mime="application/octet-stream",
        )

st.write('\n')
st.write('\n')


# SOCIAL MEDIA SECTION

col1, col2, col3 = st.columns(3)

col1.markdown(f"🔖 [Email](mailto:{'medo.mody4265@gmail.com'})")
col2.markdown(f"🔖 [LinkedIn](https://www.linkedin.com/in/mohamed-abobakr-%F0%9F%87%B5%F0%9F%87%B8-178234282/)")
col3.markdown(f"🔖 [GitHub](https://github.com/M7mdAboBakr)")
st.write('\n')
st.write('\n')

# HARD SKILLS SECTION

st.subheader(f"🛠️ Technical Skills")
st.divider()
st.write("- **👨🏻‍💻 Programming:** Python")
st.write("- **🌐 Web Scraping:** BeautifulSoup")
st.write("- **📶 Data Analysis:** NumPy, Pandas")
st.write("- **📉 Statistical Analysis:** Descriptive Statistics")
st.write("- **📊 Data Visualization:** Plotly, Familiar With (Matplotlib, Seaborn)")
st.write("- **🛢️ Database Management:** SQL Databases (MySQL, SQL Server)")
st.write("- **🦾 Machine Learning:** Scikit-learn, Supervised Learning (Regression, Classification)")
st.write("- **🧰 Tools and Software:** Jupyter Notebooks, Git/GitHub, Streamlit")

st.write('\n')
st.write('\n')

# SOFT SKILLS SECTION

st.subheader(f"🤝 Soft Skills")
st.divider()
st.write("- **🏷️ Analytical Thinking**")
st.write("- **🏷️ Problem Solving**")
st.write("- **🏷️ Adaptability**")
st.write("- **🏷️ Teamwork**")
st.write("- **🏷️ Communication**")

st.write('\n')
st.write('\n')

# EDUCATION SECTION

st.subheader(f"📜 Education & Certificates")
st.divider()
st.markdown("🎓 Bachelor of Computer Science    |    🏢 Beni-Suef University    |    🕰️ 2021 - 2025")
st.markdown("🎓 Certified Data Science Professional    |    🏢 EpsilonAI    |    🕰️ 2023 - 2024")

st.write('\n')
st.write('\n')

# PROJECTS SECTION

st.subheader(f"🖥️ Projects")
st.divider()
st.markdown("📊 **[Hotel Bookings EDA - Analysis and Dashboard for Hotel Bookings Data](https://github.com/M7mdAboBakr/HotelBookings-EDA-Dashboard)**")
st.markdown("📊 **[Ecommerce EDA - Analysis and Dashboard for Ecommerce Data](https://github.com/M7mdAboBakr/Ecommerce-EDA-Dashboard)**")
st.markdown("📖 **[DIWAN Web Scraping - Scraping Some Books Details](https://github.com/M7mdAboBakr/Web-Scraping-Python/tree/main/diwan.com)**")
st.markdown("📖 **[BooksToScrape Web Scraping - Scraping Book Title, Rate and Price](https://github.com/M7mdAboBakr/Web-Scraping-Python/tree/main/books.toscrape.com)**")
st.markdown("📝 **[WUZZUF Web Scraping - Scraping Job Title and Job Requirements and Other Details](https://github.com/M7mdAboBakr/Web-Scraping-Python/tree/main/wuzzuf.com)**")
st.markdown("⚽ **[YallaKora Web Scraping - Scraping The Teams, The Result and other Details](https://github.com/M7mdAboBakr/Web-Scraping-Python/tree/main/yallakora.com)**")
st.markdown("🎯 **[Hungman Game - Guess The Word With Limited Attempts Game](https://github.com/M7mdAboBakr/Hungman-Game)**")
st.markdown("🔐 **[Password Generator - Controllable N-Digit (Default=16) Strong Password Generator](https://github.com/M7mdAboBakr/Strong-Password-Generator)**")
st.markdown("💥 **[Thanos - Program that Deletes Half of The Files Randomly Choosen](https://github.com/M7mdAboBakr/Thanos)**")
st.markdown("🏛️ **[Library System - Managment System for Libraries with OOP](https://github.com/M7mdAboBakr/Library-System)**")
st.markdown("✂ **[Rock Paper Scissors Game - You and Computer, The First One Reaches 5 Wins](https://github.com/M7mdAboBakr/Rock-Paper-Scissors-Game)**")




    

