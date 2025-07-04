import streamlit as st

# Sayfa Ayarı
st.set_page_config(page_title="AYBU Final Notu Hesaplama", page_icon="🎓", layout="centered")

# BAŞLIK
st.markdown("""
    <h1 style='text-align: center; color: navy;'>🎓 AYBU Final Notu Hesaplama Programı</h1>
    <h4 style='text-align: center;'></h4>
    
    <hr>
""", unsafe_allow_html=True)

# Not girildi mi kontrolü için bayraklar
portfolio_girildi = False
macmillan_girildi = False
quiz_girildi = False

# Portfolyo Notları
with st.expander("📁 Portfolyo Notları (Her biri 0-20 aralığında)"):
    sunum = st.number_input("Sunum Notu", min_value=0, max_value=20, value=0)
    aybuzem = st.number_input("Aybuzem Notu", min_value=0, max_value=20, value=0)
    writing1 = st.number_input("1. Writing Notu", min_value=0, max_value=20, value=0)
    writing2 = st.number_input("2. Writing Notu", min_value=0, max_value=20, value=0)
    writing3 = st.number_input("3. Writing Notu", min_value=0, max_value=20, value=0)
    portfolio_girildi = any([sunum, aybuzem, writing1, writing2, writing3])

# Macmillan Notu
with st.expander("📘 Macmillan Notu (0-8 aralığında)"):
    macmillan = st.number_input("Macmillan Notu", min_value=0, max_value=8, value=0)
    macmillan_girildi = macmillan > 0

# Quiz Notları
with st.expander("📝 Quiz Notları (0-100 aralığında)"):
    quiz1 = st.number_input("1. Quiz Notu", min_value=0, max_value=100, value=0)
    quiz2 = st.number_input("2. Quiz Notu", min_value=0, max_value=100, value=0)
    quiz3 = st.number_input("3. Quiz Notu", min_value=0, max_value=100, value=0)
    quiz_girildi = any([quiz1, quiz2, quiz3])

# Görsel bildirimler
st.markdown("---")
if portfolio_girildi:
    st.success("📁 Portfolyo notları kayıtlı ✅")
else:
    st.warning("📁 Portfolyo notları girilmedi")

if macmillan_girildi:
    st.success("📘 Macmillan notu kayıtlı ✅")
else:
    st.warning("📘 Macmillan notu girilmedi")

if quiz_girildi:
    st.success("📝 Quiz notları kayıtlı ✅")
else:
    st.warning("📝 Quiz notları girilmedi")

# Hesaplama Butonu
st.markdown("---")
if st.button("✅ Notu Hesapla"):
    if not (portfolio_girildi and macmillan_girildi and quiz_girildi):
        st.error("Lütfen tüm notları eksiksiz girin!")
    else:
        portfolio = sunum + aybuzem + writing1 + writing2 + writing3
        toplamquiz = quiz1 / 20 + quiz2 / 20 + quiz3 / 20  # Her quiz 5 puan eder
        yannot = portfolio * 17 / 100 + macmillan + toplamquiz
        gereken = 64.5 - yannot
        final = gereken * 100 / 60 if gereken > 0 else 0

        st.markdown(f"""
            <div style='background-color:#e6f7ff; padding:20px; border-radius:10px; text-align:center;'>
                <h2 style='color:green;'>🎯 Toplam Puan: {round(yannot, 2)}</h2>
                <h3 style='color:red;'>📌 Kuru Geçmek için Finalden Alman Gereken Minimum Not: {round(final, 2)}</h3>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<p style='text-align: center; font-size: 12px;'>Developed by Dolphin Long from AYBU MIS 😉</p>", unsafe_allow_html=True)
