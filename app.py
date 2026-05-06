import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="K-Career Global",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Comprehensive Multi-language Dictionary (9 Languages Supported)
TRANSLATIONS = {
    "MN": {
        "menu_home": "Нүүр хуудас",
        "menu_jobs": "Ажлын байр",
        "menu_ai": "AI CV Засвар",
        "menu_chatbot": "AI Chatbot 💬",
        "menu_exam": "Шалгалтын төв",
        "hero_title": "Солонгост Төгс Карьераа Эхлүүлцгээе! 🚀",
        "hero_subtitle": "Гадаад оюутнуудад зориулсан цагийн ажил, мэргэжлийн карьер болон визний зөвлөгөө",
        "filter_city": "📍 Хот сонгох",
        "filter_type": "💼 Ажлын чиглэл",
        "all": "Бүгд",
        "job_prof": "Мэргэжлийн ажил (IT, Маркетинг, Орчуулга)",
        "job_part": "Цагийн ажил (Ресторан, Дэлгүүр, Туслах)",
        "chat_title": "🤖 K-Career AI Зөвлөх",
        "chat_welcome": "Сайн байна уу! Солонгос дахь амьдрал, виз, ажил болон хууль эрх зүйн талаар надаас асуугаарай.",
        "chat_placeholder": "D-2 визээр цагийн ажил хийхэд ямар бичиг баримт хэрэгтэй вэ?",
        "exam_title": "Мэргэжлийн шалгалтууд",
        "exam_desc": "Солонгост ажиллаж амьдрахад заавал хэрэг болох хэлний болон визний шалгалтууд",
        "visa_alert": "⚠️ Анхаар: Солонгост ажил эхлэхээсээ өмнө заавал Цагийн ажлын зөвшөөрөл (시간제취업허가서) авсан байх шаардлагатай!"
    },
    "EN": {
        "menu_home": "Home",
        "menu_jobs": "Jobs",
        "menu_ai": "AI Resume",
        "menu_chatbot": "AI Chatbot 💬",
        "menu_exam": "Exam Center",
        "hero_title": "Start Your Perfect Career in Korea! 🚀",
        "hero_subtitle": "Part-time jobs, professional careers, and visa consulting for international students",
        "filter_city": "📍 Select City",
        "filter_type": "💼 Job Category",
        "all": "All",
        "job_prof": "Professional Jobs (IT, Marketing, Translation)",
        "job_part": "Part-time Jobs (Restaurant, Store, Assistant)",
        "chat_title": "🤖 K-Career AI Assistant",
        "chat_welcome": "Hello! Ask me anything about visas, jobs, Korean culture, or regulations.",
        "chat_placeholder": "What documents do I need for a part-time job on a D-2 visa?",
        "exam_title": "Language & Visa Exams",
        "exam_desc": "Essential exams required for employment and visa upgrades in South Korea.",
        "visa_alert": "⚠️ Important: You must obtain a part-time work permit (시간제취업허가서) before starting any job!"
    },
    "KO": {
        "menu_home": "홈",
        "menu_jobs": "채용정보",
        "menu_ai": "AI 첨삭",
        "menu_chatbot": "AI 챗봇 💬",
        "menu_exam": "시험 센터",
        "hero_title": "한국에서 완벽한 커리어를 시작하세요! 🚀",
        "hero_subtitle": "외국인 유학생을 위한 시간제 일자리, 전문직 채용 및 비자 컨설팅",
        "filter_city": "📍 지역 선택",
        "filter_type": "💼 채용 구분",
        "all": "전체",
        "job_prof": "전문직 (IT, 마케팅, 번역)",
        "job_part": "일반 알바 (식당, 매장, 단순노무)",
        "chat_title": "🤖 K-Career AI 비서",
        "chat_welcome": "안녕하세요! 한국 생활, 비자, 채용 및 규정에 대해 무엇이든 물어보세요.",
        "chat_placeholder": "D-2 비자로 아르바이트를 하려면 어떤 서류가 필요한가요?",
        "exam_title": "자격증 및 비자 시험",
        "exam_desc": "대한민국 취업 및 비자 변경을 위해 꼭 필요한 시험 안내",
        "visa_alert": "⚠️ 주의: 근무를 시작하기 전에 반드시 '시간제취업허가서'를 발급받아야 합니다!"
    },
    "VI": {
        "menu_home": "Trang chủ", "menu_jobs": "Việc làm", "menu_ai": "Sửa CV AI", "menu_chatbot": "AI Chatbot 💬", "menu_exam": "Trung tâm thi",
        "hero_title": "Bắt đầu sự nghiệp của bạn tại Hàn Quốc! 🚀", "hero_subtitle": "Việc làm bán thời gian, sự nghiệp chuyên nghiệp và tư vấn visa cho du học sinh",
        "filter_city": "📍 Chọn thành phố", "filter_type": "💼 Loại công việc", "all": "Tất cả",
        "job_prof": "Công việc chuyên môn (IT, Marketing, Biên dịch)", "job_part": "Việc làm thêm (Nhà hàng, Cửa hàng, Trợ lý)",
        "chat_title": "🤖 Trợ lý AI K-Career", "chat_welcome": "Xin chào! Hãy hỏi tôi bất cứ điều gì về visa, việc làm hoặc cuộc sống ở Hàn Quốc.",
        "chat_placeholder": "Tôi cần giấy tờ gì để làm thêm với visa D-2?", "exam_title": "Kỳ thi tiếng Hàn & Visa",
        "exam_desc": "Các kỳ thi cần thiết để xin việc và nâng cấp visa tại Hàn Quốc.",
        "visa_alert": "⚠️ Lưu ý: Bạn phải có giấy phép làm thêm (시간제취업허가서) trước khi bắt đầu làm việc!"
    },
    "TH": {
        "menu_home": "หน้าแรก", "menu_jobs": "งาน", "menu_ai": "แก้ไข CV ด้วย AI", "menu_chatbot": "AI Chatbot 💬", "menu_exam": "ศูนย์สอบ",
        "hero_title": "เริ่มต้นอาชีพที่สมบูรณ์แบบของคุณในเกาหลี! 🚀", "hero_subtitle": "งานพาร์ทไทม์ อาชีพเฉพาะทาง และการให้คำปรึกษาด้านวีซ่าสำหรับนักศึกษาต่างชาติ",
        "filter_city": "📍 เลือกเมือง", "filter_type": "💼 ประเภทงาน", "all": "ทั้งหมด",
        "job_prof": "งานวิชาชีพ (IT, การตลาด, แปลภาษา)", "job_part": "งานพาร์ทไทม์ (ร้านอาหาร, ร้านค้า, ผู้ช่วย)",
        "chat_title": "🤖 ผู้ช่วย AI K-Career", "chat_welcome": "สวัสดี! ถามฉันได้ทุกเรื่องเกี่ยวกับวีซ่า งาน หรือการใช้ชีวิตในเกาหลี",
        "chat_placeholder": "ต้องใช้เอกสารอะไรบ้างในการทำงานพาร์ทไทม์ด้วยวีซ่า D-2?", "exam_title": "การสอบภาษาและวีซ่า",
        "exam_desc": "การสอบสำคัญที่จำเป็นสำหรับการทำงานและการปรับเปลี่ยนวีซ่าในเกาหลีใต้",
        "visa_alert": "⚠️ สำคัญ: คุณต้องได้รับใบอนุญาตทำงานพาร์ทไทม์ (시간제취업허가서) ก่อนเริ่มทำงาน!"
    },
    "RU": {
        "menu_home": "Главная", "menu_jobs": "Вакансии", "menu_ai": "AI Резюме", "menu_chatbot": "AI Чат-бот 💬", "menu_exam": "Экзамены",
        "hero_title": "Начните карьеру в Корее! 🚀", "hero_subtitle": "Подработка, профессиональная карьера и визовые консультации для студентов",
        "filter_city": "📍 Выберите город", "filter_type": "💼 Категория работы", "all": "Все",
        "job_prof": "Профессиональная работа (IT, Маркетинг, Перевод)", "job_part": "Подработка (Рестораны, Магазины, Ассистенты)",
        "chat_title": "🤖 AI-Помощник K-Career", "chat_welcome": "Привет! Спрашивайте обо всем, что связано с визами, работой или жизнью в Корее.",
        "chat_placeholder": "Какие документы нужны для подработки по визе D-2?", "exam_title": "Экзамены для работы и визы",
        "exam_desc": "Ключевые экзамены, необходимые для трудоустройства и смены визы в Южной Корее.",
        "visa_alert": "⚠️ Важно: Перед началом работы вы обязаны получить разрешение на подработку (시간제취업허가서)!"
    },
    "JA": {
        "menu_home": "ホーム", "menu_jobs": "求人情報", "menu_ai": "AI履歴書添削", "menu_chatbot": "AIチャットボット 💬", "menu_exam": "試験センター",
        "hero_title": "韓国でのキャリアをスタートさせましょう！ 🚀", "hero_subtitle": "外国人留学生向けのアルバイト、専門職採用、ビザコンサルティング",
        "filter_city": "📍 地域選択", "filter_type": "💼 求人区分", "all": "すべて",
        "job_prof": "専門職 (IT、マーケティング、翻訳)", "job_part": "アルバイト (飲食店、ショップ、軽作業)",
        "chat_title": "🤖 K-Career AIアシスタント", "chat_welcome": "こんにちは！ビザ、仕事、韓国での生活について何でも聞いてください。",
        "chat_placeholder": "D-2ビザでアルバイトをするにはどんな書類が必要ですか？", "exam_title": "韓国語・ビザ試験",
        "exam_desc": "韓国での就職やビザ変更に必須となる主要な試験案内",
        "visa_alert": "⚠️ 重要：アルバイトを始める前に、必ず事前に「時間外就業許可書」を取得してください！"
    },
    "ZH": {
        "menu_home": "首页", "menu_jobs": "招聘岗位", "menu_ai": "AI 简历修改", "menu_chatbot": "AI 智能客服 💬", "menu_exam": "考试中心",
        "hero_title": "在韩国开启您的完美职业生涯！ 🚀", "hero_subtitle": "专为外国留学生提供的兼职、专业工作及签证咨询服务",
        "filter_city": "📍 选择城市", "filter_type": "💼 岗位类别", "all": "全部",
        "job_prof": "专业工作 (IT、市场营销、翻译)", "job_part": "兼职工作 (餐厅、便利店、助教)",
        "chat_title": "🤖 K-Career AI 助手", "chat_welcome": "您好！有关签证、工作或韩国生活的任何问题都可以向我提问。",
        "chat_placeholder": "持有 D-2 签证做兼职需要准备哪些材料？", "exam_title": "语言及签证考试",
        "exam_desc": "在韩国求职和晋升签证所需的核心考试指南",
        "visa_alert": "⚠️ 重要提示：在开始任何工作之前，必须先获得“时间制就业许可证”！"
    },
    "MY": {
        "menu_home": "ပင်မစာမျက်နှာ", "menu_jobs": "အလုပ်အကိုင်", "menu_ai": "AI ကိုယ်ရေးရာဇဝင်", "menu_chatbot": "AI Chatbot 💬", "menu_exam": "စာမေးပွဲစင်တာ",
        "hero_title": "ကိုရီးယားမှာ သင့်ရဲ့ အကောင်းဆုံး ကာရီယာကို စတင်လိုက်ပါ။ 🚀", "hero_subtitle": "နိုင်ငံခြားကျောင်းသားများအတွက် အချိန်ပိုင်းအလုပ်၊ ပရော်ဖက်ရှင်နယ်အလုပ်နှင့် ဗီဇာအတိုင်ပင်ခံဝန်ဆောင်မှု",
        "filter_city": "📍 မြို့ရွေးချယ်ရန်", "filter_type": "💼 အလုပ်အမျိုးအစား", "all": "အားလုံး",
        "job_prof": "ပရော်ဖက်ရှင်နယ်အလုပ် (IT၊ စျေးကွက်ရှာဖွေရေး၊ ဘာသာပြန်)", "job_part": "အချိန်ပိုင်းအလုပ် (စားသောက်ဆိုင်၊ စတိုးဆိုင်၊ အကူ)",
        "chat_title": "🤖 K-Career AI အကူအညီပေးသူ", "chat_welcome": "မင်္ဂလာပါ။ ဗီဇာ၊ အလုပ် သို့မဟုတ် ကိုရီးယားနိုင်ငံရှိ လူနေမှုဘဝအကြောင်း သိလိုသမျှ မေးမြန်းနိုင်ပါသည်။",
        "chat_placeholder": "D-2 ဗီဇာဖြင့် အချိန်ပိုင်းအလုပ်လုပ်ရန် ဘာစာရွက်စာတမ်းတွေ လိုအပ်ပါသလဲ။", "exam_title": "ဘာသာစကားနှင့် ဗီဇာစာမေးပွဲများ",
        "exam_desc": "တောင်ကိုရီးယားနိုင်ငံတွင် အလုပ်အကိုင်ရရှိရန်နှင့် ဗီဇာအဆင့်မြှင့်တင်ရန် လိုအပ်သော အဓိကစာမေးပွဲများ",
        "visa_alert": "⚠️ အရေးကြီးသည်- မည်သည့်အလုပ်မဆို မစတင်မီ အချိန်ပိုင်းအလုပ်လုပ်ကိုင်ခွင့်ပါမစ် (시간제취업허가서) ကို မဖြစ်မနေ ရယူရပါမည်။"
    }
}

# 3. Dynamic Enhanced CSS Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    .header-box {
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        padding: 2.5rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .custom-card {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #E5E7EB;
        margin-bottom: 1.2rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px -3px rgba(0, 0, 0, 0.1);
        border-color: #4F46E5;
    }
    .exam-card {
        background: #f8fafc;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #4F46E5;
        margin-bottom: 20px;
    }
    .badge-city {
        background-color: #EEF2F6;
        color: #4F46E5;
        padding: 4px 10px;
        border-radius: 10px;
        font-size: 11px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-type {
        background-color: #ECFDF5;
        color: #059669;
        padding: 4px 10px;
        border-radius: 10px;
        font-size: 11px;
        font-weight: 600;
        display: inline-block;
        margin-left: 5px;
    }
    .chat-bubble-user {
        background-color: #EEF2F6;
        padding: 12px;
        border-radius: 15px 15px 0px 15px;
        margin: 10px 0px 10px auto;
        max-width: 70%;
        text-align: right;
        font-size: 14px;
    }
    .chat-bubble-ai {
        background-color: #E0E7FF;
        padding: 12px;
        border-radius: 15px 15px 15px 0px;
        margin: 10px 0px;
        max-width: 70%;
        font-size: 14px;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)

# 4. Jobs Mock Database with Locations and Categories
if 'jobs_db' not in st.session_state:
    st.session_state.jobs_db = [
        {"title": "Global SNS Marketing Specialist", "company": "K-Beauty Inc.", "city": "Seoul", "category": "Professional", "visa": "D-2, D-10, F-2", "pay": "2,300,000 KRW/month", "desc": "Manage English, Mongolian, and Vietnamese social media accounts. Flexible hours for graduating students."},
        {"title": "Web Development Intern (React/Node)", "company": "Seoul Tech Labs", "city": "Seoul", "category": "Professional", "visa": "D-2, D-10", "pay": "2,100,000 KRW/month", "desc": "Seeking passionate frontend/backend interns. Global work environment and visa sponsorship available."},
        {"title": "Tour Guide & Translator (Part-time)", "company": "Busan Travels", "city": "Busan", "category": "Professional", "visa": "D-2 (with permit)", "pay": "15,000 KRW/hour", "desc": "Guide international tourists in Busan. Must speak good English or Mongolian/Vietnamese."},
        {"title": "Cafe Barista (Weekend)", "company": "Blue Bottle Incheon", "city": "Incheon", "category": "Part-time", "visa": "D-2 (with permit)", "pay": "10,100 KRW/hour", "desc": "Weekend morning shift. Basic Korean communication required. Friendly staff and free coffee benefit."},
        {"title": "Convenience Store Staff (Night shift)", "company": "GS25 Daegu", "city": "Daegu", "category": "Part-time", "visa": "D-2, G-1", "pay": "10,030 KRW/hour", "desc": "GS25 night shift. General cashier duties and shelf restocking. Friendly owner and meal allowance provided."},
        {"title": "Mechanical Engineering Assistant", "company": "Daejeon R&D Corp", "city": "Daejeon", "category": "Professional", "visa": "D-2, D-10", "pay": "Negotiable", "desc": "Assist researchers in chemical and mechanical engineering tasks. Great chance to gain laboratory experience in Korea."}
    ]

# 5. Sidebar and Language Selector
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=300&auto=format&fit=crop", use_container_width=True)
    lang_choice = st.selectbox("🌐 Select Language / Хэл сонгох", options=list(TRANSLATIONS.keys()), index=0)
    t = TRANSLATIONS[lang_choice]
    
    st.markdown("<h2 style='text-align: center; color: #4F46E5; margin-top: 10px;'>K-Career 🎓</h2>", unsafe_allow_html=True)
    
    # Navigation Menu
    selected = option_menu(
        menu_title=None,
        options=[t["menu_home"], t["menu_jobs"], t["menu_ai"], t["menu_chatbot"], t["menu_exam"]],
        icons=["house", "briefcase", "cpu", "chat-dots", "award"],
        menu_icon="cast", default_index=0,
        styles={
            "container": {"background-color": "#fafafa"},
            "nav-link-selected": {"background-color": "#4F46E5"},
        }
    )

# --- MENU: HOME ---
if selected == t["menu_home"]:
    st.markdown(f"""
    <div class="header-box">
        <h1>{t['hero_title']}</h1>
        <p>{t['hero_subtitle']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="custom-card">
            <h3>💼 Local & Professional Jobs</h3>
            <p>Find legal part-time jobs and corporate professional career opportunities filtered by cities in South Korea.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="custom-card">
            <h3>🤖 Intelligent AI Assistant</h3>
            <p>Engage with our AI Career Coach about visa regulations (D-2 to E-7, F-2-99) and get your Korean resume proofread instantly.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="custom-card">
            <h3>📑 Official Exam Guides</h3>
            <p>Everything you need to know to easily register and prepare for official Korean exams like TOPIK and KIIP.</p>
        </div>
        """, unsafe_allow_html=True)

# --- MENU: JOBS (with City and Profession Filters) ---
elif selected == t["menu_jobs"]:
    st.subheader(f"💼 {t['menu_jobs']}")
    
    # Visa Alert Banner
    st.markdown(f"""
    <div class="custom-card" style="background-color: #FFFBEB; border-color: #FDE68A;">
        <p style="color: #B45309; margin: 0px; font-weight: 600;">{t['visa_alert']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filter Controls Layout
    col_city, col_type = st.columns(2)
    
    with col_city:
        city_list = [t["all"]] + list(sorted(set([j["city"] for j in st.session_state.jobs_db])))
        selected_city = st.selectbox(t["filter_city"], options=city_list)
        
    with col_type:
        type_options = {t["all"]: "All", t["job_prof"]: "Professional", t["job_part"]: "Part-time"}
        selected_type_label = st.selectbox(t["filter_type"], options=list(type_options.keys()))
        selected_type = type_options[selected_type_label]

    # Filter Logic
    filtered_jobs = st.session_state.jobs_db
    if selected_city != t["all"]:
        filtered_jobs = [j for j in filtered_jobs if j["city"] == selected_city]
    if selected_type != "All":
        filtered_jobs = [j for j in filtered_jobs if j["category"] == selected_type]

    # Display Jobs
    st.write(f"### Found {len(filtered_jobs)} matching jobs:")
    for job in filtered_jobs:
        st.markdown(f"""
        <div class="custom-card">
            <span class="badge-city">📍 {job['city']}</span>
            <span class="badge-type">🎯 {job['category']}</span>
            <h4 style="margin-top: 10px; color: #1E1B4B;">{job['title']}</h4>
            <p style="margin-bottom: 5px;"><b>Company:</b> {job['company']} | <b>Pay Rate:</b> {job['pay']}</p>
            <p style="margin-bottom: 5px; font-size: 13px; color: #4F46E5;"><b>Eligible Visas:</b> {job['visa']}</p>
            <p style="color: #4B5563; font-size: 14px; margin-top: 10px;">{job['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- MENU: AI CV REVIEW ---
elif selected == t["menu_ai"]:
    st.subheader(f"📝 {t['menu_ai']}")
    st.write("Paste your Korean self-introduction (자기소개서) or resume below to get instant AI-powered expert feedback and spelling corrections.")
    
    user_cv = st.text_area("Your Korean Text:", height=250, placeholder="저는 한국에서 아르바이트를 찾고 있습니다...")
    api_key = st.text_input("Google Gemini API Key (Optional):", type="password")
    
    if st.button("Analyze & Correct", type="primary"):
        if not api_key:
            st.warning("⚠️ Showing live demo preview. Provide a Gemini API Key to enable real-time processing.")
            st.markdown(f"""
            <div class="custom-card" style="background-color: #F0FDF4; border-color: #86EFAC;">
                <h4 style="color: #166534;">✨ AI Corrected Version (Demo Example):</h4>
                <p><b>Original:</b> 저는 한국에서 아르바이트를 찾고 있습니다.</p>
                <p><b>Recommended Correction:</b> 대한민국에서 학업과 일의 양립을 통해 글로벌 역량을 키우고자 아르바이트에 지원하게 되었습니다.</p>
                <p><b>Feedback:</b> Using a more ambitious and confident opening sentence improves your chances of getting hired in South Korea.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-pro')
                
                prompt = f"""
                You are an expert HR manager in South Korea. 
                Please review, correct grammar, and improve the professional tone of the following Korean Resume/Introduce (자기소개서) for an international student.
                Provide the feedback in Mongolian and corrected Korean text clearly.
                
                Resume content:
                {user_cv}
                """
                with st.spinner("AI is analyzing your CV..."):
                    response = model.generate_content(prompt)
                    st.write("### AI Response:")
                    st.info(response.text)
            except Exception as e:
                st.error(f"Error connecting to API: {e}")

# --- MENU: AI CHATBOT ---
elif selected == t["menu_chatbot"]:
    st.subheader(t["chat_title"])
    st.markdown(f"<p style='color: grey;'>{t['chat_welcome']}</p>", unsafe_allow_html=True)
    
    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        
    # Render chat history
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-bubble-user">{message["text"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble-ai">{message["text"]}</div>', unsafe_allow_html=True)
            
    # Input Area
    user_message = st.text_input("Ask anything to AI Assistant:", placeholder=t["chat_placeholder"])
    api_key_chat = st.text_input("Gemini API Key (Optional for live chat):", type="password", key="chat_api_key")
    
    if st.button("Send", type="primary"):
        if user_message:
            # 1. Append user query
            st.session_state.chat_history.append({"role": "user", "text": user_message})
            
            # 2. Get AI Response
            if api_key_chat:
                try:
                    import google.generativeai as genai
                    genai.configure(api_key=api_key_chat)
                    model = genai.GenerativeModel('gemini-pro')
                    
                    system_prompt = "You are a professional assistant helping international students with visas (D-2, D-10, E-7, etc.), part-time jobs, and legal regulations in South Korea. Answer accurately, empathetically, and in detail."
                    full_prompt = f"{system_prompt}\n\nStudent asks: {user_message}"
                    
                    with st.spinner("AI is thinking..."):
                        response = model.generate_content(full_prompt)
                        st.session_state.chat_history.append({"role": "ai", "text": response.text})
                except Exception as e:
                    st.session_state.chat_history.append({"role": "ai", "text": f"Error: {e}"})
            else:
                # Fallback mockup response
                mock_reply = "Уучлаарай, чатыг амьдаар ажиллуулахын тулд Gemini API түлхүүрээ оруулна уу. Оюутны D-2 визний тухайд: Цагийн ажлын зөвшөөрөл (시간제취업허가서) авахад Сургуулийн Олон Улсын Албаны зөвшөөрөл, ТОPIK оноо, Сурлагын дүн (GPA) хамгийн чухал байдаг."
                st.session_state.chat_history.append({"role": "ai", "text": mock_reply})
            
            # Instant rerun to display new chat bubbles
            st.rerun()

# --- MENU: EXAM CENTER ---
elif selected == t["menu_exam"]:
    st.subheader(f"📑 {t['exam_title']}")
    st.write(t["exam_desc"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="exam-card">
            <h3>1. TOPIK (한국어능력시험)</h3>
            <p><b>Purpose:</b> Standardized Korean proficiency exam required by universities and corporate companies in Korea.</p>
            <ul>
                <li><b>TOPIK I (Levels 1-2):</b> Beginner level</li>
                <li><b>TOPIK II (Levels 3-6):</b> Intermediate to Advanced</li>
            </ul>
            <p>📅 Held up to 6 times a year within South Korea.</p>
            <p>🔗 <b>Official Website:</b> <a href="https://www.topik.go.kr" target="_blank">topik.go.kr</a></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to TOPIK Official Registration"):
            st.write("Redirecting to [topik.go.kr](https://www.topik.go.kr)...")

    with col2:
        st.markdown(f"""
        <div class="exam-card">
            <h3>2. KIIP (사회통합프로그램)</h3>
            <p><b>Purpose:</b> Korea Immigration and Integration Program. Highly useful for upgrading student visas (D-2) to resident visas (F-2) or permanent residency (F-5).</p>
            <ul>
                <li>Consists of levels 0 to 5 (Korean language and society culture).</li>
                <li>Provides huge bonus points for visa conversion without needing high TOPIK scores.</li>
            </ul>
            <p>📅 Registered by semesters based on pre-test results.</p>
            <p>🔗 <b>Official Website:</b> <a href="https://www.socinet.go.kr" target="_blank">socinet.go.kr</a></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Go to KIIP (Socinet) Registration"):
            st.write("Redirecting to [socinet.go.kr](https://www.socinet.go.kr)...")
