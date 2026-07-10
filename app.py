import streamlit as st
from domain_checker import check_domain
from trademark_checker import check_trademark
from brand_generator import generate_names
from utils import names_to_dataframe
from services.uspto import search_uspto
from brand_score import score_brand
from brand_value import estimate_brand_value
from ranker import rank_brands
#@st.cache_data(ttl=3600)
def cached_search_uspto(name):
    return search_uspto(name)
#@st.cache_data(ttl=3600)
def cached_check_trademark(name):
 return check_trademark(name)
#@st.cache_data(ttl=300)
def cached_check_domain(domain):
    return check_domain(domain)
st.set_page_config(
    page_title="BrandHunter AI",
    page_icon="🔎",
    layout="wide"  # تحويل المقاس إلى wide لعرض البيانات بشكل أفضل
)

st.title("🔎 BrandHunter AI")
st.write("منصتك الذكية لابتكار، فحص، وتقييم النطاقات والعلامات التجارية")
st.divider()
# ==========================
# الجزء الأول: توليد أسماء جديدة
# ==========================

st.header("💡 ابتكار أسماء نطاقات جديدة")

col_input, col_btn = st.columns([3, 1])

with col_input:
    industry = st.selectbox(
        "اختر مجال مشروعك المستقبلي:",
        ["AI", "SaaS", "Cybersecurity", "Finance", "Healthcare"]
    )

with col_btn:
    st.write("")
    generate_btn = st.button(
        "✨ توليد 20 اسمًا جديدًا",
        use_container_width=True
    )

if generate_btn:
    with st.spinner("جاري توليد الأسماء وفحص النطاقات..."):

        names = generate_names(industry, 20)

        results = names_to_dataframe(names)

        results = rank_brands(results)

        import pandas as pd

        df = pd.DataFrame(results)
        sort_by = st.selectbox(
       "ترتيب حسب",
       ["Score", "Brand", ".com"]
)

ascending = sort_by == "Brand"
df = df.sort_values(by=sort_by, ascending=ascending)
    st.subheader("💡 أفضل الأسماء")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# ==========================
# الجزء الثاني: تحليل وفحص اسم محدد
# ==========================
st.header("🔍 فحص وتحليل اسم محدد")

name = st.text_input("اكتب اسم العلامة التجارية المقترحة هنا:", placeholder="مثال: technova")
extensions = [".com", ".ai", ".io", ".app"]

if st.button("بدء عملية الفحص الشامل 🚀", use_container_width=True):
    if not name:
        st.warning("⚠️ الرجاء كتابة اسم أولاً للبدء.")
    else:
        clean = name.lower().replace(" ", "")

        # تقسيم النتائج إلى تبويبات (Tabs) لتنظيم الواجهة ومنع تشتت المستخدم
        tab_domains, tab_legal, tab_valuation = st.tabs([
            "🌐 توفر النطاقات (Domains)",
            "🛡️ الحماية القانونية والعلامات",
            "📊 التقييم والقيمة التقديرية"
        ])

        with tab_domains:
            cols = st.columns(len(extensions))
            for idx, ext in enumerate(extensions):
                full_domain = clean + ext
                result = cached_check_domain(full_domain)

                with cols[idx]:
                    if result["status"] == "Available":
                        st.success(f"✅ {full_domain}\n\nمتاح للتسجيل")
                    else:
                        st.error(f"❌ {full_domain}\n\nمستخدم حالياً")

        with tab_legal:
            col_tm, col_uspto = st.columns(2)

            with col_tm:
                matches = cached_check_trademark(clean)
                if not matches:
                    st.info("لا توجد علامات تجارية مشابهة مباشرة.")
                else:
                    for item in matches:
                        st.write(f"**{item['name']}** — تشابه {item['score']}%")

            with col_uspto:
                uspto = cached_search_uspto(clean)
                st.info(uspto["message"])

        with tab_valuation:
            brand = score_brand(clean)

            c1, c2 = st.columns(2)

            with c1:
                st.metric("درجة البراند العامة", f"{brand['score']}/100")
                st.write(brand["stars"])

            with c2:
                domain_result = cached_check_domain(clean + ".com")
                domain_available = domain_result["status"] == "Available"

                min_value, max_value = estimate_brand_value(
                    clean, brand["score"], domain_available
                )

                st.metric(
                    "💰 القيمة السوقية التقديرية",
                    f"${min_value:,} - ${max_value:,}"
                )

            for reason in brand["reasons"]:
                st.success(f"• {reason}")
