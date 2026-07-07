import streamlit as st
import socket

st.set_page_config(
    page_title="BrandHunter AI",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 BrandHunter AI")
st.write("ابحث عن توفر نطاق .com")

name = st.text_input("اسم العلامة التجارية")

def check_domain(domain):
    try:
        socket.gethostbyname(domain)
        return False
    except:
        return True

if st.button("بحث"):
    if name == "":
        st.warning("اكتب اسمًا أولاً")
    else:
        domain = name.lower().replace(" ", "") + ".com"

        with st.spinner("جاري الفحص..."):
            available = check_domain(domain)

        st.subheader("النتيجة")

        if available:
            st.success(f"✅ {domain} يبدو غير مرتبط بعنوان IP حاليًا.")
            st.info("تحقق أيضًا لدى مسجل نطاقات قبل الشراء، لأن هذه الطريقة ليست حاسمة.")
        else:
            st.error(f"❌ {domain} مرتبط بعنوان IP، وغالبًا مستخدم.")
