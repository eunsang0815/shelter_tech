import streamlit as st

st.set_page_config(page_title="ShelterTech Dashboard", layout="wide")

st.title("📊 ShelterTech Internal Dashboard")
st.markdown("이 페이지는 기술 데모 및 내부 테스트용입니다.")

# 예시 섹션: 프로젝트 상태 요약
st.subheader("✅ 프로젝트 진행 현황")
st.write("- 랜딩페이지 통합 완료")
st.write("- GitHub Pages 배포 확인")
st.write("- NDA intake 외부 처리로 전환됨")

# 예시 섹션: 향후 작업
st.subheader("📌 다음 단계")
st.write("- 머신러닝 페이지 구성")
st.write("- VC 피치덱 정리 및 배포")
