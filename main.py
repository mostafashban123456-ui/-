import streamlit as st
import time

# --- إعدادات الهوية البصرية السيادية ---
st.set_page_config(page_title="AlManara AI | سلطان المعرفة", page_icon="🕌", layout="centered")

# --- تخصيص التصميم (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #1E3A8A; color: white; }
    .stTextInput>div>div>input { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- قاعدة بيانات الذكاء الاصطناعي (محاكاة المراجع المدمجة) ---
def almanara_ai_response(query):
    # هنا يتم استحضار منطق مراجع ويلر، كلاين، والكتب الشرعية
    query = query.lower()
    if "زواج" in query or "عزاب" in query:
        return "رؤية سلطان تضمن تيسير الزواج عبر صندوق الكرامة، شرعاً هذا من باب التكافل، وتقنياً سيتم تمويله من أرباح الاندماج النووي."
    elif "فقر" in query or "تسول" in query:
        return "النظام يعمل على 'صفر فقر' من خلال توزيع عادل للثروة الناتجة عن تكنولوجيا النانو والاندماج، لضمان كرامة كل مواطن."
    elif "الدين" in query or "حكم" in query:
        return "بناءً على مكتبة الإمام البوطي والقواعد الفقهية، الإجابة تقتضي الموازنة بين المقاصد الشرعية ومصلحة الأمة في العصر الحديث."
    else:
        return "جاري تحليل السؤال بناءً على مراجع (Weller & Klein) والعلوم الشرعية.. الإجابة تهدف لتحقيق المساواة وفض أي نزاع محتمل."

# --- نظام تسجيل الدخول المحكم ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

def check_login():
    st.title("🔐 بوابة المنارة")
    with st.container():
        user = st.text_input("اسم المستخدم (Mostafa)")
        pwd = st.text_input("كلمة المرور", type="password")
        if st.button("تفعيل السيادة"):
            if user == "Mostafa" and pwd == "admin":
                st.session_state['auth'] = True
                st.rerun()
            else:
                st.error("بيانات الوصول غير صحيحة")

# --- الواجهة الرئيسية للمنصة ---
def main_app():
    st.image("https://github.com/mostafashban123456-ui/AlManara-Islamic-AI/raw/main/1000097993.jpg", use_column_width=True)
    st.title("🏛️ عقل المنارة الإسلامي الذكي")
    st.info("مرحباً بك يا سلطان.. النظام الآن متصل بمراجع الكيمياء، الفيزياء، والشريعة لخدمة رؤيتك.")

    # صندوق المحادثة الذكي
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("اسأل عن الدين، الكيمياء، أو مستقبل الرؤية..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("جاري استحضار المعرفة..."):
                time.sleep(1)
                response = almanara_ai_response(prompt)
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# --- التشغيل ---
if not st.session_state['auth']:
    check_login()
else:
    main_app()
