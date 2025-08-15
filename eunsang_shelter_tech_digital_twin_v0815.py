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
st.markdown("🐾 **EunSang Shelter Tech – Digital Twin Lab**")
st.markdown("Welcome to the official repository for EunSang Animal Shelter Tech, a next-generation platform combining machine learning, AR/VR, and biometric data to improve animal welfare outcomes.")

st.subheader("🚀 Live App")
st.markdown("[Explore the Digital Twin Lab](https://sheltertech.streamlit.app)")

st.subheader("🧠 Features")
st.markdown("""
- Digital Twin Dashboard: Real-time health and behavior insights  
- Return Rate Prediction: ML model to forecast adoption success  
- AR Mode: Visualize animals in your space  
- Vitals Monitor: Heart rate, temperature, activity level  
- AI Insights: Mood, diet, and medical recommendations  
""")

st.subheader("🧬 Machine Learning Models")
st.markdown("""
- `return_rate_model.pkl`  
- `adoption_success_model.pkl`  
- `behavior_forecast_model.pkl`  
""")

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
st.markdown("📧 For product inquiries: **eunsang.sheltertech@gmail.com**")

st.markdown("""
<div style='background-color:#f9f5e5; padding:10px; border-left:5px solid #f4c430;'>
<b>Important Notice:</b>  
We will be planning to introduce a <b>Mini Water Treatment System Machine Learning Model</b> that fits remote areas far away from a huge central water treatment plant.
</div>
""", unsafe_allow_html=True)

st.subheader("🛠️ Tech Stack")
st.markdown("""
- Python, Streamlit, scikit-learn, pandas  
- AR/VR integration (Unity/WebXR roadmap)  
""")

st.subheader("📂 Repository Structure")
st.markdown("Welcome to EunSang Shelter Tech AI")

st.subheader("📊 Vitals Monitor")
st.metric("Heart Rate", "102 bpm")
st.metric("Temperature", "38.6 °C")

st.subheader("📈 Health Forecast")
forecast = pd.DataFrame({
    "Day": [f"Day {i}" for i in range(1, 8)],
    "Health Score": [85, 88, 70, 75, 80, 82, 84]
})
st.line_chart(forecast.set_index("Day"))

st.subheader("🚨 Alerts")
st.warning("Vaccination due in 3 days")
st.info("Risk flag: Stress level elevated")

st.subheader("🧬 AI Insights")
st.write("**Mood Prediction:** Calm")
st.progress(0.3)
st.write("**Diet Suggestion:** High-protein, low-carb")
st.write("**Medical Recommendation:** Vet visit recommended next week")

if st.toggle("🕶️ AR Mode"):
    st.success("AR Mode Activated (Simulated)")

st.markdown("---")
st.caption("Powered by Streamlit + EunSang Shelter Tech AI")
