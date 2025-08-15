import streamlit as st
import joblib
import numpy as np
import pandas as pd  # ← 추가

# 모델 로드
model = joblib.load('adoption_model_0804.pkl')

st.title("🐶 입양 확률 예측기 (v0804)")
st.write("SprayBrush 사용 시 건강 개선 효과가 반영된 모델입니다.")

# 입력 받기
age = st.slider("동물 나이 (개월)", 0, 240, 24)
breed = st.selectbox("품종 코드 (예시)", [1, 2, 3])
health = st.slider("건강 점수 (1~5)", 1, 5, 3)
spray = st.checkbox("SprayBrush 사용")
skin = st.slider("피부 개선 점수 (1~5)", 1, 5, 3)
days = st.slider("보호소 체류 기간", 0, 60, 10)

# 예측 (경고 제거한 방식)
input_data = pd.DataFrame([{
    'age_in_months': age,
    'breed_encoded': breed,
    'health_score': health,
    'spraybrush_used': int(spray),
    'skin_improvement_score': skin,
    'days_in_shelter': days
}])
prob = model.predict_proba(input_data)[0][1]

# 출력
st.subheader(f"🔮 예측된 입양 확률: **{prob:.2%}**")
