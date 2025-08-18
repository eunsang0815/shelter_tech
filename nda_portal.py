import streamlit as st
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

# 🌍 Country restriction using IP geolocation
def get_user_country():
    try:
        response = requests.get("https://ipapi.co/json/")
        data = response.json()
        return data.get("country_name", "Unknown")
    except:
        return "Unknown"

allowed_countries = ["United States", "Canada", "United Kingdom"]
user_country = get_user_country()

if user_country not in allowed_countries:
    st.warning(f"Access restricted. Your country ({user_country}) is not authorized.")
    st.stop()
st.set_page_config(page_title="ShelterTech NDA Portal", page_icon="📄")

st.title("📄 ShelterTech Document Access Portal")
st.markdown("Please fill out the form below to access the SB Brush Specification Sheet. Access is limited to users in the **United States** and **Canada**.")

# Country restriction
country = st.selectbox("Country", ["Select", "United States", "Canada"])
if country not in ["United States", "Canada"]:
    st.warning("Access is limited to users in the US and Canada.")
    st.stop()

# Form
with st.form("nda_form"):
    name = st.text_input("Full Name")
    org = st.text_input("Organization")
    job = st.text_input("Occupation")
    address = st.text_area("Address")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success("✅ Thank you! You may now download the SB Specification Sheet and NDA Agreement.")
    st.markdown("[📄 Download SB Specification Sheet](https://github.com/eunsang0815/shelter_tech/raw/main/return_rate_model/ProductSpecifiation_SB_Waterlox_Vet_Private_Use_Only_.pdf)")
    st.markdown("[📄 Download NDA Agreement](https://github.com/eunsang0815/shelter_tech/raw/main/return_rate_model/NDA_ShelterTech.pdf)")
    st.info("Please complete the NDA and email it to: **eunsang.sheltertech@gmail.com**. Once verified, we’ll send you the Business Plan and full specifications.")

    # Log to Google Sheets
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("google_sheets_secret.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("ShelterTech NDA Submissions").sheet1
        sheet.append_row([str(datetime.datetime.now()), name, org, job, address, email, phone, country])
    except Exception as e:
        st.warning("⚠️ Submission logged locally, but Google Sheets logging failed.")
        st.text(str(e))
