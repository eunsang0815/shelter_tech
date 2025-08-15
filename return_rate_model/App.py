import streamlit as st
import joblib
import numpy as np
import pandas as pd

# 모델 로드
model = joblib.load("return_model_0805.pkl")

# 페이지 설정
st.set_page_config(page_title="Return Rate Prediction", layout="centered")

# 타이틀
st.markdown("# 🐾 Return Probability Estimator")
st.markdown("### Fill in the information below to estimate the likelihood of an animal being returned.")

# 입력 폼
with st.form("prediction_form"):
    age = st.slider("Age of Animal", 0, 25, 3)
    breed_code = st.selectbox("Breed Code", list(range(1, 11)))
    distance = st.slider("Distance from Rescue to Home (km)", 0, 100, 10)
    spray_used = st.selectbox("SprayBrush Used?", [0, 1])
    has_chip = st.selectbox("Microchip Present?", [0, 1])
    water_nearby = st.selectbox("Is Water Nearby?", [0, 1])
    weather_code = st.selectbox("Weather Condition Code", list(range(0, 10)))
    rescuer_gender = st.selectbox("Rescuer Gender", [0, 1])
    skin_condition = st.selectbox("Skin Condition Code", list(range(1, 6)))  # ✅ 반드시 있어야 함

    submit = st.form_submit_button("🔮 Predict Return Probability")

# 예측
if submit:
    columns = [
        'age_in_months', 'breed_encoded', 'health_score', 'spraybrush_used',
        'weather_score', 'water_nearby', 'rescuer_gender', 'has_identity',
        'days_until_return'
    ]

    data = pd.DataFrame([[age, breed_code, skin_condition, spray_used,
                          weather_code, water_nearby, rescuer_gender,
                          has_chip, distance]],  # distance를 days_until_return로 사용 중
                        columns=columns)

    prob = model.predict_proba(data)[0][1]

    st.markdown("---")
    st.markdown(
        f"<h2 style='text-align: left; color: darkblue;'>🎯 Predicted Return Probability: <span style='font-size: 40px;'>{prob:.2f}%</span></h2>",
        unsafe_allow_html=True
    )
