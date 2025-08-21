import streamlit as st
import requests

# 🌍 Country restriction using IP geolocation
def get_user_country():
    try:
        response = requests.get("https://ipapi.co/json/")
        data = response.json()
        return data.get("country_name", "Unknown")
    except:
        return "Unknown"

# ✅ Page setup
st.set_page_config(page_title="NDA Access Portal", page_icon="🔐", layout="centered")
st.title("🔐 NDA Access Request Portal")

st.markdown("""
Welcome to the NDA access portal for Shelter Tech.  
Please fill out the form below. Access is restricted to users in **United States**, **United Kingdom**, and **Canada**.
""")

# 📝 NDA Request Form
with st.form("nda_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    country = st.selectbox("Country", ["Select", "United States", "United Kingdom", "Canada", "Other"])
    submitted = st.form_submit_button("Submit")

# 🚦 Submission Logic
if submitted:
    if country in ["United States", "United Kingdom", "Canada"]:
        st.success(f"✅ Access granted, {name}. You may download the NDA below.")
        st.markdown("[📄 Download NDA_ShelterTech.pdf](https://eunsang0815.github.io/shelter_tech/NDA_ShelterTech.pdf)")
        st.info("Please complete the NDA and email it to: **eunsang.sheltertech@gmail.com**")
    elif country == "Select":
        st.warning("⚠️ Please select your country.")
    else:
        st.error("❌ Access denied. NDA is only available to users in US, UK, or Canada.")
