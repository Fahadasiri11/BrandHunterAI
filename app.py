import streamlit as st
from domain_checker import check_domain
from trademark_checker import check_trademark

st.set_page_config(
    page_title="BrandHunter AI",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 BrandHunter AI")
st.write("فحص النطاقات والعلامات التجارية")

name = st.text_input("اكتب اسم العلامة التجارية")

extensions = [".com", ".ai", ".io", ".app"]

if st.button("بحث"):
    if not name:
        st.warning("اكتب اسمًا أولاً")
    else:
        clean = name.lower().replace(" ", "")
matches = check_trademark(clean)

st.subheader("🛡️ العلامات التجارية المشابهة")

for item in matches:
    score = item["score"]

    if score >= 80:
        risk = "🔴 مرتفعة جداً"
    elif score >= 60:
        risk = "🟠 متوسطة"
    else:
        risk = "🟢 منخفضة"

    st.write(f"**{item['name']}**")
    st.write(f"نسبة التشابه: {score}%")
    st.write(f"مستوى المخاطرة: {risk}")
    st.divider()
        st.subheader("🌐 النطاقات")

        for ext in extensions:
            result = check_domain(clean + ext)

            if result["status"] == "Available":
                st.success(f"✅ {clean + ext} متاح")
            else:
                st.error(f"❌ {clean + ext} مستخدم")

        st.subheader("🛡️ العلامة التجارية")

        

for item in matches:
    score = item["score"]

    if score >= 80:
        risk = "🔴 مرتفعة جداً"
    elif score >= 60:
        risk = "🟠 متوسطة"
    else:
        risk = "🟢 منخفضة"

    st.write(f"**{item['name']}**")
    st.write(f"نسبة التشابه: {score}%")
    st.write(f"مستوى المخاطرة: {risk}")
    st.divider()
