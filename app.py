import streamlit as st
from domain_checker import check_domain

st.set_page_config(
    page_title="BrandHunter AI",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 BrandHunter AI")
st.write("فحص توفر النطاقات")

name = st.text_input("اكتب اسم العلامة التجارية")

extensions = [".com", ".ai", ".io", ".app"]

if st.button("بحث"):
    if not name:
        st.warning("اكتب اسمًا أولاً")
    else:
        clean = name.lower().replace(" ", "")

        for ext in extensions:
            result = check_domain(clean + ext)

            if result["status"] == "Available":
                st.success(f"✅ {clean + ext} متاح")
            else:
                st.error(f"❌ {clean + ext} مستخدم")
