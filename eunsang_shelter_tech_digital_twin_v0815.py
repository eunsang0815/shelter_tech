import streamlit as st

# 사이드바 메뉴
menu = st.sidebar.selectbox("메뉴를 선택하세요", ["🏠 Home", "📊 Dashboard", "📍 Map", "📁 Data"])

# 각 메뉴에 따른 페이지 구성
if menu == "🏠 Home":
    st.title("🏠 Welcome to ShelterTech Digital Twin")
    st.write("이곳은 대시보드의 홈 화면입니다.")

elif menu == "📊 Dashboard":
    st.title("📊 실시간 대시보드")
    st.write("여기에 센서 데이터 시각화가 들어갑니다.")

elif menu == "📍 Map":
    st.title("📍 대피소 위치 지도")
    st.write("지도 기반 대피소 위치 정보 제공")

elif menu == "📁 Data":
    st.title("📁 데이터 다운로드")
    st.write("CSV, Excel 등 데이터 다운로드 기능 제공")
