import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="AYBU Final Hesaplama", page_icon="🎓", layout="centered")

# Başlık
st.markdown("<h1 style='text-align: center; color: navy;'>🎓 AYBU Final Notu Hesaplama</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Created by Yunus • AYBU MIS Student</h4>", unsafe_allow_html=True)
st.markdown("---")

# PORTFOLYO
with st.container():
    st.subheader("📁 Portfolyo Notları (0-20 arası)")
    col1, col2, col3 = st.columns(3)
    with col1:
        sunum = st.number_input("Sunum", 0, 20, 0)
        writing1 = st.number_input("Writing 1", 0, 20, 0)
    with col2:
        aybuzem = st.number_input("Aybuzem", 0, 20, 0)
        writing2 = st.number_input("Writing 2", 0, 20, 0)
    with col3:
        writing3 = st.number_input("Writing 3", 0, 20, 0)

# MACMILLAN
with st.container():
    st.subheader("📘 Macmillan Notu (0-8 arası)")
    macmillan = st.slider("Macmillan", 0, 8, 0)

# QUIZLER
with st.container():
    st.subheader("📝 Quiz Notları (0-100 arası)")
    quiz1 = st.number_input("Quiz 1", 0, 100, 0)
    quiz2 = st.number_input("Quiz 2", 0, 100, 0)
    quiz3 = st.number_input("Quiz 3", 0, 100, 0)

# HESAPLAMA
st.markdown("---")
if st.button("✅ Hesapla"):
    toplam_portfolio = sunum + aybuzem + writing1 + writing2 + writing3
    toplam_quiz = quiz1 / 20 + quiz2 / 20 + quiz3 / 20
    toplam_not = toplam_portfolio + macmillan + toplam_quiz

    st.markdown(f"""
        <div style='background-color:#e6f7ff; padding:20px; border-radius:10px; text-align:center;'>
            <h2 style='color:green;'>🎯 Toplam Notun: {round(toplam_not, 2)}</h2>
        </div>
    """, unsafe_allow_html=True)
