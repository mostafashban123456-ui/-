import streamlit as st
from datetime import datetime

# --- إعدادات المنصة ---
st.set_page_config(page_title="منصة المنارة - الشاملة", layout="wide")

# --- دالة حساب مواقيت الصلاة (تجريبية) ---
def get_prayer_times():
    # يمكن ربطها بـ API حقيقي لاحقاً، حالياً تظهر مواعيد تقريبية
    return {"الفجر": "05:15", "الظهر": "12:05", "العصر": "03:10", "المغرب": "05:30", "العشاء": "07:00"}

# --- نظام إدارة الوصول ---
if 'islamic_access' not in st.session_state:
    st.session_state['islamic_access'] = False
if 'dikr_count' not in st.session_state:
    st.session_state['dikr_count'] = 0

if not st.session_state['islamic_access']:
    st.image("1000097993.jpg", use_container_width=True)
    st.title("🕋 بوابة المنارة الإسلامية")
    user = st.text_input("اسم الطالب")
    pw = st.text_input("كلمة السر", type="password")
    if st.button("دخول"):
        st.session_state['islamic_access'] = True
        st.rerun()
    st.stop()

# --- القائمة الجانبية المتقدمة ---
st.sidebar.title("⭐ ركن العبادات")

# 1. مواقيت الصلاة
st.sidebar.subheader("🕒 مواقيت الصلاة اليوم")
times = get_prayer_times()
for prayer, time in times.items():
    st.sidebar.write(f"**{prayer}:** {time}")

st.sidebar.divider()

# 2. عداد الأذكار
st.sidebar.subheader("📿 عداد الأذكار")
st.sidebar.write(f"عدد التسبيحات: {st.session_state['dikr_count']}")
if st.sidebar.button("سبّح (الحمد لله / استغفر الله)"):
    st.session_state['dikr_count'] += 1
if st.sidebar.button("تصفير العداد"):
    st.session_state['dikr_count'] = 0

st.sidebar.divider()

choice = st.sidebar.selectbox("اختر القسم الرئيسي:", [
    "💎 شرح الحكم العطائية (البوطي)",
    "📖 المصحف والتجويد المرئي",
    "📚 مكتبة الشريعة والقراءات",
    "🤖 المساعد الشرعي AI",
    "🎥 البث المباشر"
])

# --- عرض المحتوى بناءً على الاختيار ---

if choice == "💎 شرح الحكم العطائية (البوطي)":
    st.header("✨ مجالس الإمام البوطي في شرح الحكم العطائية")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.video("https://www.youtube.com/watch?v=vVAn_D_fDsc") # فيديو الإمام البوطي
    with col2:
        st.subheader("📚 الحكمة الحالية")
        st.info("💡 'لا يكن تأخر أمد العطاء مع الإلحاح في الدعاء موجباً ليأسك...'")
        st.write("🤖 **شرح AI:** يطمئننا الإمام أن الله يستجيب لنا بما يختاره هو لا بما نختاره نحن.")

elif choice == "📖 المصحف والتجويد المرئي":
    st.header("📖 التلاوة التعليمية")
    st.video("https://www.youtube.com/watch?v=8p_hS449DWA")
    st.file_uploader("🎤 سجل تلاوتك للتصحيح:", type=['mp3', 'wav'])

# ... باقي الأقسام كما في الكود السابق ...
