import streamlit as st
import pandas as pd
import datetime

# Sample animal data
animals = [
    {"name": "Max", "species": "Dog", "status": "Needs Attention"},
    {"name": "Bella", "species": "Cat", "status": "Healthy"},
    {"name": "Charlie", "species": "Dog", "status": "Monitoring"},
    {"name": "Lucy", "species": "Cat", "status": "Healthy"},
]

# Sidebar: Animal Profile
st.sidebar.title("🐾 Animal Profiles")
search = st.sidebar.text_input("Search")
for animal in animals:
    if search.lower() in animal["name"].lower() or search == "":
        st.sidebar.write(f"**{animal['name']}** ({animal['species']}) - *{animal['status']}*")

# Header
st.title("🧠 Digital Twin Lab")
# Show README.md content
with open("README.md", "r") as f:
    readme_text = f.read()
st.markdown(readme_text)
st.markdown("Welcome to EunSang Shelter Tech AI")

# Main Dashboard
st.subheader("📊 Vitals Monitor")
st.metric("Heart Rate", "102 bpm")
st.metric("Temperature", "38.6 °C")
st.progress(0.7)  # Activity Level

# Prediction Timeline
st.subheader("📈 Health Forecast")
forecast = pd.DataFrame({
    "Day": [f"Day {i}" for i in range(1, 8)],
    "Health Score": [85, 88, 70, 75, 80, 82, 84]
})
st.line_chart(forecast.set_index("Day"))

# Alerts
st.subheader("🚨 Alerts")
st.warning("Vaccination due in 3 days")
st.info("Risk flag: Stress level elevated")

# AI Insights
st.subheader("🧬 AI Insights")
st.write("**Mood Prediction:** Calm")
st.progress(0.3)  # Stress Level
st.write("**Diet Suggestion:** High-protein, low-carb")
st.write("**Medical Recommendation:** Vet visit recommended next week")

# AR Toggle
if st.toggle("🕶️ AR Mode"):
    st.success("AR Mode Activated (Simulated)")

# SB Brush Product Section with NDA
st.subheader("📦 SB Brush System")

st.markdown("We offer the SB Brush System, a hygiene and care solution for shelter environments.")

st.info("To protect our intellectual property, please agree to the NDA before downloading.")

agree = st.checkbox("✅ I agree to the Non-Disclosure Agreement (NDA)")

if agree:
    with open("ProductSpecifiation_SB_Waterlox_Vet_Private_Use_Only_.pdf", "rb") as f:
        pdf_data = f.read()
    st.download_button("📄 Download SB Brush Specification", pdf_data, file_name="SB_Brush_Spec.pdf")

    with open("NDA_ShelterTech.pdf", "rb") as nda:
        nda_data = nda.read()
    st.download_button("📝 Download Blank NDA Form", nda_data, file_name="ShelterTech_NDA.pdf")
else:
    st.warning("Please agree to the NDA to access the product specification.")

# Footer
st.markdown("---")
st.caption("Powered by Streamlit + EunSang Shelter Tech AI")

