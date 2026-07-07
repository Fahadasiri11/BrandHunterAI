import streamlit as st
from domain_checker import check_domain
from trademark_checker import check_trademark
from brand_generator import generate_names
from utils import names_to_dataframe
from services.uspto import search_uspto
from brand_score import score_brand
from brand_value import estimate_brand_value
st.set_page_config(
    page_title="BrandHunter AI",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 BrandHunter AI")
st.write("فحص النطاقات والعلامات التجارية")

# ==========================
# توليد أسماء جديدة
# ==========================

industry = st.selectbox(
    "اختر المجال",
    [
        "AI",
        "SaaS",
        "Cybersecurity",
        "Finance",
        "Healthcare"
    ]
)

if st.button("✨ توليد 20 اسمًا جديدًا"):
    with st.spinner("جاري توليد الأسماء وفحص النطاقات..."):
        names = generate_names(industry, 20)
        df = names_to_dataframe(names)

    st.subheader("💡 الأسماء المقترحة")
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
st.divider()

# ==========================
# البحث عن اسم
# ==========================

name = st.text_input("اكتب اسم العلامة التجارية")

extensions = [".com", ".ai", ".io", ".app"]
if st.button("بحث"):

    if not name:
        st.warning("اكتب اسمًا أولاً")

    else:
        clean = name.lower().replace(" ", "")

        # فحص النطاقات
        st.subheader("🌐 النطاقات")

        for ext in extensions:
            result = check_domain(clean + ext)

            if result["status"] == "Available":
                st.success(f"✅ {clean + ext} متاح")
            else:
                st.error(f"❌ {clean + ext} مستخدم")

        # العلامات التجارية
        st.subheader("🛡️ العلامات التجارية المشابهة")

        matches = check_trademark(clean)

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

        # USPTO
        st.subheader("🇺🇸 البحث في USPTO")

        uspto = search_uspto(clean)

        st.info(uspto["message"])

        # تقييم الاسم
        st.subheader("⭐ تقييم الاسم")

        brand = score_brand(clean)

        st.metric("الدرجة", f"{brand['score']}/100")

        st.write(brand["stars"])

        for reason in brand["reasons"]:
            st.success(reason)

        # القيمة التقديرية
        st.subheader("💰 القيمة التقديرية")

        value = estimate_brand_value(clean, brand["score"])

        st.metric(
            "القيمة المتوقعة",
            f"${value['min']:,} - ${value['max']:,}"
        )
