import streamlit as st

st.set_page_config(
    page_title="BrandHunter AI",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 BrandHunter AI")

name = st.text_input("اكتب اسم العلامة التجارية")

if st.button("بحث"):
    if name:
        st.success(f"سيتم البحث عن: {name}")
    else:
        st.warning("اكتب اسم أولاً")
