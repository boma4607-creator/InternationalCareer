import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="K-Career: Global Study & Work in Korea",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Comprehensive Multi-language Dictionary (9 Languages)
TRANSLATIONS = {
    "MN": {
        "title": "K-Career",
        "subtitle": "Гадаад оюутнуудын нэгдсэн платформ",
        "hero_title": "Солонгост Төгс Карьераа Эхлүүлцгээе! 🚀",
        "hero_subtitle": "Цагийн ажил, карьер хөгжүүлэлт, виз болон шалгалтын зөвлөгөө",
        "menu_home": "Нүүр хуудас",
        "menu_jobs": "Ажлын зарууд",
        "menu_ai": "AI-ээр CV засах",
        "menu_exams": "Шалгалтын заавар",
        "menu_training": "Career сургалт",
        "menu_tips": "Туршлага & Зөвлөгөө",
        "card_jobs": "💼 Ажлын зарууд",
        "card_jobs_desc": "Оюутны визэнд тохирсон цагийн болон үндсэн ажлын байр.",
        "card_ai": "🤖 AI CV Засвар",
        "card_ai_desc": "자기소개서 болон CV-гээ солонгос стандартын дагуу AI-аар засуулах.",
        "card_exams": "📝 Шалгалтын заавар",
        "card_exams_desc": "TOPIK болон KIIP шалгалтын бүртгэлийн зааварчилгаа, хуваарь.",
        "tab_search": "🔎 Ажил хайх",
        "tab_post": "➕ Зар нэмэх",
        "active_jobs": "Идэвхтэй зарууд:",
        "job_title": "Ажлын байрны нэр",
        "company": "Компани / Газрын нэр",
        "location": "Байршил",
        "visa_req": "Зөвшөөрөгдөх визний төрөл",
        "salary": "Цалин",
        "job_desc": "Ажлын тайлбар",
        "btn_post": "Зар нийтлэх",
        "post_success": "Амжилттай нийтлэгдлээ!",
        "post_error": "Заавал бөглөх талбаруудыг бөглөнө үү.",
        "ai_desc": "Солонгос хэл дээрх CV-гээ оруулаад хиймэл оюунаас зөвлөмж аваарай.",
        "ai_placeholder": "Энд бичвэрээ оруулна уу...",
        "ai_btn": "AI-аар засуулах",
        "ai_warning": "⚠️ API түлхүүр байхгүй тул загвар хариултыг харуулж байна.",
        "visa_alert": "⚠️ Анхаар: Ажиллаж эхлэхээсээ өмнө заавал Цагийн ажлын зөвшөөрөл (시간제취업허가서) аваарай!",
        "btn_register": "Бүртгүүлэх"
    },
    "KO": {
        "title": "K-Career",
        "subtitle": "외국인 유학생을 위한 통합 플랫폼",
        "hero_title": "한국에서 완벽한 커리어를 시작하세요! 🚀",
        "hero_subtitle": "시간제 일자리, 커리어 개발, 비자 및 시험 컨설팅",
        "menu_home": "홈",
        "menu_jobs": "채용 공고",
        "menu_ai": "AI 자기소개서 첨삭",
        "menu_exams": "시험 가이드",
        "menu_training": "커리어 교육",
        "menu_tips": "경험 & 팁",
        "card_jobs": "💼 채용 공고",
        "card_jobs_desc": "유학생 비자에 적합한 아르바이트 및 정규직 채용 정보.",
        "card_ai": "🤖 AI 자기소개서 첨삭",
        "card_ai_desc": "한국 기업 트렌드에 맞춘 이력서를 인공지능으로 교정.",
        "card_exams": "📝 시험 가이드",
        "card_exams_desc": "TOPIK 및 사회통합프로그램(KIIP) 정보와 등록 안내.",
        "tab_search": "🔎 채용 정보 찾기",
        "tab_post": "➕ 구인 등록",
        "active_jobs": "현재 채용 중인 공고:",
        "job_title": "채용 직무",
        "company": "회사/상호명",
        "location": "근무지",
        "visa_req": "허용 비자 종류",
        "salary": "급여 조건",
        "job_desc": "담당 업무 설명",
        "btn_post": "공고 등록하기",
        "post_success": "공고가 성공적으로 등록되었습니다.",
        "post_error": "필수 항목을 작성해주세요.",
        "ai_desc": "한국어로 작성한 이력서를 입력하면 AI가 첨삭을 진행합니다.",
        "ai_placeholder": "여기에 내용을 입력하세요...",
        "ai_btn": "AI 분석 시작",
        "ai_warning": "⚠️ API 키가 없어 샘플 답변을 표시합니다.",
        "visa_alert": "⚠️ 주의: 근무 시작 전 반드시 '시간제취업허가서'를 발급받아야 합니다!",
        "btn_register": "신청하기"
    },
    "EN": {
        "title": "K-Career",
        "subtitle": "Integrated Platform for International Students",
        "hero_title": "Start Your Perfect Career in Korea! 🚀",
        "hero_subtitle": "Part-time jobs, career development, visas, and language exams",
        "menu_home": "Home",
        "menu_jobs": "Job Board",
        "menu_ai": "AI Resume Helper",
        "menu_exams": "Exam Guide",
        "menu_training": "Career Training",
        "menu_tips": "Tips & Stories",
        "card_jobs": "💼 Job Board",
        "card_jobs_desc": "Legal jobs suitable for student visa holders.",
        "card_ai": "🤖 AI Resume Review",
        "card_ai_desc": "Polished and corrected by AI for Korean standard corporate style.",
        "card_exams": "📝 Exam Guide",
        "card_exams_desc": "TOPIK and KIIP registration guides, schedules, and links.",
        "tab_search": "🔎 Search Jobs",
        "tab_post": "➕ Post a Job",
        "active_jobs": "Currently Active Jobs:",
        "job_title": "Job Title",
        "company": "Company Name",
        "location": "Location",
        "visa_req": "Eligible Visas",
        "salary": "Salary / Pay",
        "job_desc": "Job Description",
        "btn_post": "Post Job",
        "post_success": "Your job post has been published!",
        "post_error": "Please fill in all required fields.",
        "ai_desc": "Paste your Korean self-introduction below to get AI-powered feedback.",
        "ai_placeholder": "Paste your text here...",
        "ai_btn": "Get AI Feedback",
        "ai_warning": "⚠️ No API Key found. Showing demo results.",
        "visa_alert": "⚠️ Rule: You must obtain a part-time work permit before starting work!",
        "btn_register": "Register Now"
    },
    "ZH": {
        "title": "K-Career",
        "subtitle": "留学生一站式服务平台",
        "hero_title": "在韩国开启您的完美职业生涯！🚀",
        "hero_subtitle": "兼职工作、职业发展、签证及语言考试指南",
        "menu_home": "首页",
        "menu_jobs": "招聘信息",
        "menu_ai": "AI 简历修改",
        "menu_exams": "考试指南",
        "menu_training": "职业培训",
        "menu_tips": "经验分享",
        "card_jobs": "💼 招聘信息",
        "card_jobs_desc": "适合留学生签证持有者的合法工作机会。",
        "card_ai": "🤖 AI 简历修改",
        "card_ai_desc": "利用人工智能对韩语简历进行专业级润色。",
        "card_exams": "📝 考试指南",
        "card_exams_desc": "TOPIK 韩语等级考试与社会整合程序 (KIIP) 攻略。",
        "tab_search": "🔎 寻找工作",
        "tab_post": "➕ 发布招聘",
        "active_jobs": "当前招聘岗位：",
        "job_title": "工作岗位",
        "company": "公司名称",
        "location": "工作地点",
        "visa_req": "支持签证类型",
        "salary": "薪资待遇",
        "job_desc": "岗位职责说明",
        "btn_post": "发布",
        "post_success": "成功发布招聘信息！",
        "post_error": "请填写必填字段。",
        "ai_desc": "输入韩语自我介绍获取 AI 实时修改建议。",
        "ai_placeholder": "在此输入内容...",
        "ai_btn": "开始 AI 润色",
        "ai_warning": "⚠️ 未检测到 API 密匙，正在展示示例。",
        "visa_alert": "⚠️ 注意：开始工作前务必提前申请“时间制就业许可证”！",
        "btn_register": "立即报名"
    },
    "VI": {
        "title": "K-Career",
        "subtitle": "Nền tảng tích hợp cho du học sinh",
        "hero_title": "Bắt đầu sự nghiệp hoàn hảo của bạn tại Hàn Quốc! 🚀",
        "hero_subtitle": "Việc làm thêm, phát triển sự nghiệp, visa và chứng chỉ",
        "menu_home": "Trang chủ",
        "menu_jobs": "Tin tuyển dụng",
        "menu_ai": "AI Sửa CV",
        "menu_exams": "Hướng dẫn thi",
        "menu_training": "Đào tạo nghề",
        "menu_tips": "Kinh nghiệm & Tips",
        "card_jobs": "💼 Việc làm",
        "card_jobs_desc": "Cơ hội việc làm hợp pháp cho học sinh, sinh viên.",
        "card_ai": "🤖 AI Sửa CV",
        "card_ai_desc": "Sửa bài giới thiệu bản thân (자기소개서) theo chuẩn Hàn Quốc bằng AI.",
        "card_exams": "📝 Hướng dẫn thi",
        "card_exams_desc": "Thông tin đăng ký và lịch thi TOPIK, chương trình hội nhập KIIP.",
        "tab_search": "🔎 Tìm việc",
        "tab_post": "➕ Đăng tin",
        "active_jobs": "Công việc hiện tại:",
        "job_title": "Tên công việc",
        "company": "Tên công ty",
        "location": "Địa điểm",
        "visa_req": "Visa chấp nhận",
        "salary": "Mức lương",
        "job_desc": "Mô tả công việc",
        "btn_post": "Đăng bài",
        "post_success": "Đăng tin thành công!",
        "post_error": "Vui lòng nhập đầy đủ thông tin.",
        "ai_desc": "Nhập CV tiếng Hàn của bạn để nhận đánh giá và chỉnh sửa từ AI.",
        "ai_placeholder": "Nhập văn bản tại đây...",
        "ai_btn": "Nhận phản hồi từ AI",
        "ai_warning": "⚠️ Không tìm thấy API Key. Đang hiển thị bản demo.",
        "visa_alert": "⚠️ Lưu ý: Bạn bắt buộc phải xin Giấy phép làm thêm trước khi đi làm!",
        "btn_register": "Đăng ký ngay"
    },
    "TH": {
        "title": "K-Career",
        "subtitle": "แพลตฟอร์มแบบครบวงจรสำหรับนักศึกษาต่างชาติ",
        "hero_title": "เริ่มต้นอาชีพการทำงานที่สมบูรณ์แบบในเกาหลี! 🚀",
        "hero_subtitle": "งานพาร์ทไทม์ การพัฒนาอาชีพ วีซ่า และไกด์แนะนำการสอบภาษา",
        "menu_home": "หน้าแรก",
        "menu_jobs": "ประกาศรับสมัครงาน",
        "menu_ai": "AI แก้ไขเรซูเม่",
        "menu_exams": "คู่มือการสอบ",
        "menu_training": "คอร์สอบรมอาชีพ",
        "menu_tips": "รีวิวและประสบการณ์",
        "card_jobs": "💼 สมัครงาน",
        "card_jobs_desc": "งานพาร์ทไทม์และงานประจำที่ถูกกฎหมายสำหรับผู้ถือวีซ่านักเรียน",
        "card_ai": "🤖 AI ขัดเกลาเรซูเม่",
        "card_ai_desc": "แก้ไขจดหมายแนะนำตัว (자기소개서) ให้ดูเป็นมืออาชีพด้วยระบบ AI",
        "card_exams": "📝 คู่มือการสอบ",
        "card_exams_desc": "กำหนดการสอบและวิธีสมัครสอบ TOPIK และโครงการ KIIP",
        "tab_search": "🔎 ค้นหางาน",
        "tab_post": "➕ ลงประกาศงาน",
        "active_jobs": "งานที่เปิดรับสมัครตอนนี้:",
        "job_title": "ตำแหน่งงาน",
        "company": "ชื่อบริษัท",
        "location": "สถานที่ทำงาน",
        "visa_req": "วีซ่าที่รองรับ",
        "salary": "ค่าจ้าง",
        "job_desc": "รายละเอียดงาน",
        "btn_post": "โพสต์งาน",
        "post_success": "ประกาศงานของคุณเรียบร้อยแล้ว!",
        "post_error": "กรุณากรอกข้อมูลให้ครบถ้วน",
        "ai_desc": "วางข้อความเรซูเม่ภาษาเกาหลีของคุณเพื่อรับคำแนะนำจาก AI",
        "ai_placeholder": "กรอกข้อความที่นี่...",
        "ai_btn": "เริ่มใช้งาน AI",
        "ai_warning": "⚠️ ไม่พบ API Key กำลังแสดงผลการสาธิต",
        "visa_alert": "⚠️ ข้อสำคัญ: คุณต้องขอใบอนุญาตทำงานพาร์ทไทม์ก่อนเริ่มงานเสมอ!",
        "btn_register": "ลงทะเบียน"
    },
    "MY": {
        "title": "K-Career",
        "subtitle": "နိုင်ငံတကာကျောင်းသားများအတွက် ပလက်ဖောင်း",
        "hero_title": "ကိုရီးယားမှာ သင့်ရဲ့ အကောင်းဆုံး ကစားသမားဘဝကို စတင်လိုက်ပါ! 🚀",
        "hero_subtitle": "အချိန်ပိုင်းအလုပ်များ၊ အသက်မွေးဝမ်းကျောင်း ဖွံ့ဖြိုးတိုးတက်မှု၊ ဗီဇာနှင့် စာမေးပွဲလမ်းညွှန်",
        "menu_home": "ပင်မစာမျက်နှာ",
        "menu_jobs": "အလုပ်အကိုင်များ",
        "menu_ai": "AI ဖြင့် CV ပြင်ဆင်ရန်",
        "menu_exams": "စာမေးပွဲလမ်းညွှန်",
        "menu_training": "အသက်မွေးဝမ်းကျောင်းသင်တန်း",
        "menu_tips": "အတွေ့အကြုံများနှင့် အကြံပြုချက်များ",
        "card_jobs": "💼 အလုပ်ခေါ်စာများ",
        "card_jobs_desc": "ကျောင်းသားဗီဇာကိုင်ဆောင်သူများအတွက် တရားဝင်အချိန်ပိုင်းအလုပ်များ။",
        "card_ai": "🤖 AI CV အကူအညီပေးသူ",
        "card_ai_desc": "မိမိကိုယ်ကိုမိတ်ဆက်စာ (자기소개서) ကို AI ဖြင့် စနစ်တကျ ပြင်ဆင်ပါ။",
        "card_exams": "📝 စာမေးပွဲလမ်းညွှန်",
        "card_exams_desc": "TOPIK နှင့် KIIP စာမေးပွဲလျှောက်ထားခြင်းဆိုင်ရာ အချက်အလက်များ။",
        "tab_search": "🔎 အလုပ်ရှာရန်",
        "tab_post": "➕ အလုပ်ခေါ်စာတင်ရန်",
        "active_jobs": "လက်ရှိအလုပ်များ:",
        "job_title": "ရာထူးအမည်",
        "company": "ကုမ္ပဏီအမည်",
        "location": "လုပ်ငန်းခွင်တည်နေရာ",
        "visa_req": "လျှောက်ထားနိုင်သည့် ဗီဇာအမျိုးအစား",
        "salary": "လစာ",
        "job_desc": "လုပ်ငန်းတာဝန်များ",
        "btn_post": "အလုပ်တင်မည်",
        "post_success": "အလုပ်ခေါ်စာ အောင်မြင်စွာတင်ပြီးပါပြီ!",
        "post_error": "လိုအပ်သော အကွက်များကို ဖြည့်စွက်ပါ။",
        "ai_desc": "ကိုရီးယားဘာသာဖြင့်ရေးထားသော CV ကို ထည့်သွင်းပြီး AI ၏ အကြံပြုချက်ကိုရယူပါ။",
        "ai_placeholder": "စာသားများကို ဤနေရာတွင် ထည့်ပါ...",
        "ai_btn": "AI ဖြင့် စစ်ဆေးမည်",
        "ai_warning": "⚠️ API Key မရှိပါ။ နမူနာပြသနေပါသည်။",
        "visa_alert": "⚠️ သတိပြုရန် - အလုပ်မစတင်မီ တရားဝင် အချိန်ပိုင်းလုပ်ကိုင်ခွင့် ခွင့်ပြုချက် (시간제취업허가서) ကို အရင်လျှောက်ထားရပါမည်။",
        "btn_register": "စာရင်းသွင်းရန်"
    },
    "RU": {
        "title": "K-Career",
        "subtitle": "Единая платформа для иностранных студентов в Корее",
        "hero_title": "Начните идеальную карьеру в Корее! 🚀",
        "hero_subtitle": "Подработка, развитие карьеры, визы и подготовка к экзаменам",
        "menu_home": "Главная",
        "menu_jobs": "Вакансии",
        "menu_ai": "ИИ-Редактор резюме",
        "menu_exams": "Гид по экзаменам",
        "menu_training": "Обучение",
        "menu_tips": "Советы и опыт",
        "card_jobs": "💼 Работа",
        "card_jobs_desc": "Легальная подработка и постоянная работа для студентов.",
        "card_ai": "🤖 ИИ-Резюме",
        "card_ai_desc": "Автоматическая коррекция вашего резюме под корейские стандарты.",
        "card_exams": "📝 Гид по экзаменам",
        "card_exams_desc": "Пошаговые инструкции по сдаче экзаменов TOPIK и программы KIIP.",
        "tab_search": "🔎 Поиск работы",
        "tab_post": "➕ Добавить вакансию",
        "active_jobs": "Активные вакансии:",
        "job_title": "Название вакансии",
        "company": "Компания",
        "location": "Локация",
        "visa_req": "Подходящие визы",
        "salary": "Оплата",
        "job_desc": "Описание работы",
        "btn_post": "Опубликовать",
        "post_success": "Вакансия успешно опубликована!",
        "post_error": "Заполните все обязательные поля.",
        "ai_desc": "Вставьте ваше резюме на корейском, чтобы ИИ проверил грамматику и стиль.",
        "ai_placeholder": "Введите текст здесь...",
        "ai_btn": "Проверить через ИИ",
        "ai_warning": "⚠️ API-ключ не найден. Показана демо-версия.",
        "visa_alert": "⚠️ Важно: Обязательно получите разрешение на подработку (시간제취업허가서) до начала работы!",
        "btn_register": "Записаться"
    },
    "JA": {
        "title": "K-Career",
        "subtitle": "留学生のためのキャリア支援プラットフォーム",
        "hero_title": "韓国での完璧なキャリアをスタートさせましょう！🚀",
        "hero_subtitle": "アルバイト情報、キャリア開発、ビザ、および各種語学試験対策",
        "menu_home": "ホーム",
        "menu_jobs": "求人情報",
        "menu_ai": "AI自己紹介書添削",
        "menu_exams": "試験ガイド",
        "menu_training": "キャリア講座",
        "menu_tips": "体験談＆ノウハウ",
        "card_jobs": "💼 求人を探す",
        "card_jobs_desc": "学生ビザ保持者に適した合法的アルバイト情報。",
        "card_ai": "🤖 AI自己紹介書添削",
        "card_ai_desc": "韓国企業のニーズに沿った自己紹介書（자기소개서）をAIが高度に添削。",
        "card_exams": "📝 試験ガイド",
        "card_exams_desc": "TOPIKや社会統合プログラム（KIIP）のスケジュールと申込方法。",
        "tab_search": "🔎 求人検索",
        "tab_post": "➕ 求人登録",
        "active_jobs": "現在掲載中の求人：",
        "job_title": "職種",
        "company": "会社名",
        "location": "勤務地",
        "visa_req": "対象ビザ",
        "salary": "給与条件",
        "job_desc": "業務内容の詳細",
        "btn_post": "求人を登録する",
        "post_success": "求人情報が正常に登録されました！",
        "post_error": "必須項目を入力してください。",
        "ai_desc": "作成した自己紹介書をペーストして、AIのプロフェッショナルなフィードバックを受け取ります。",
        "ai_placeholder": "ここに文章をペーストしてください...",
        "ai_btn": "AIで添削する",
        "ai_warning": "⚠️ APIキーが設定されていないため、デモ結果を表示しています。",
        "visa_alert": "⚠️ 重要：業務開始前に必ず「時間外就労許可（시간제취업허가서）」を取得してください！",
        "btn_register": "申し込む"
    }
}

# 3. Dynamic Sidebar
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=300&auto=format&fit=crop", use_container_width=True)
    
    # Elegant Language Selector supporting 9 options
    lang_choice = st.selectbox(
        "🌐 Language Selection / хэл солих",
        options=["MN", "KO", "EN", "ZH", "VI", "TH", "MY", "RU", "JA"],
        index=0
    )
    
    t = TRANSLATIONS[lang_choice]
    
    st.markdown(f"<h2 style='text-align: center; color: #3B82F6;'>K-Career 🎓</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 13px; color: grey;'>{t['subtitle']}</p>", unsafe_allow_html=True)
    
    # Navigation menu translated dynamically
    selected = option_menu(
        menu_title=None,
        options=[t["menu_home"], t["menu_jobs"], t["menu_ai"], t["menu_exams"], t["menu_training"], t["menu_tips"]],
        icons=["house", "briefcase", "cpu", "journal-text", "award", "chat-square-quote"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#4F46E5", "font-size": "18px"}, 
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#4F46E5"},
        }
    )

# 4. Custom Styling (CSS)
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
        padding: 1.8rem;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border: 1px solid #E5E7EB;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 1.5rem;
    }
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px -3px rgba(0, 0, 0, 0.1);
        border-color: #3B82F6;
    }
    .badge {
        background-color: #EEF2F6;
        color: #1E40AF;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-right: 5px;
    }
    .badge-geo {
        background-color: #FEF3C7;
        color: #92400E;
    }
    .exam-header {
        border-left: 5px solid #4F46E5;
        padding-left: 10px;
        margin-top: 15px;
        margin-bottom: 10px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 5. Fake Job Database Session State
if 'jobs' not in st.session_state:
    st.session_state.jobs = [
        {"title": "Seoul Restaurant Assistant Manager", "company": "K-Food House", "location": "Seoul, Mapo-gu", "visa": "D-2, D-10, G-1", "pay": "10,000 KRW/hour", "desc": "Flexible schedule matching student timetables. Requires intermediate level Korean language skills."},
        {"title": "Global Digital Marketing Intern", "company": "Global Tech Korea", "location": "Seoul, Gangnam", "visa": "D-2 (with permit), D-10", "pay": "Negotiable", "desc": "Hiring international students with skills in content creation in both English and Mongolian."}
    ]

# --- MENU: HOME ---
if selected == t["menu_home"]:
    st.markdown(f"""
    <div class="header-box">
        <h1>{t['hero_title']}</h1>
        <p>{t['hero_subtitle']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="custom-card">
            <h3>{t['card_jobs']}</h3>
            <p>{t['card_jobs_desc']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="custom-card">
            <h3>{t['card_ai']}</h3>
            <p>{t['card_ai_desc']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="custom-card">
            <h3>{t['card_exams']}</h3>
            <p>{t['card_exams_desc']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="custom-card">
            <h3>📈 {t['menu_training']}</h3>
            <p>Courses to land professional jobs and prepare for interviews.</p>
        </div>
        """, unsafe_allow_html=True)

# --- MENU: JOBS ---
elif selected == t["menu_jobs"]:
    st.subheader(t["menu_jobs"])
    tab1, tab2 = st.tabs([t["tab_search"], t["tab_post"]])
    
    with tab1:
        st.write(t["active_jobs"])
        for job in st.session_state.jobs:
            st.markdown(f"""
            <div class="custom-card">
                <span class="badge">{job['company']}</span>
                <span class="badge badge-geo">📍 {job['location']}</span>
                <h4 style="margin-top: 10px;">{job['title']}</h4>
                <p><b>Visa Requirements:</b> {job['visa']} | <b>Pay Rate:</b> {job['pay']}</p>
                <p style="color: #4B5563; font-size: 14px;">{job['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
    with tab2:
        st.write(f"### {t['tab_post']}")
        with St.form("job_form", clear_on_submit=True):
            title = st.text_input(t["job_title"])
            company = st.text_input(t["company"])
            location = st.text_input(t["location"])
            visa = st.text_input(t["visa_req"])
            pay = st.text_input(t["salary"])
            desc = st.text_area(t["job_desc"])
            
            submitted = st.form_submit_button(t["btn_post"])
            if submitted:
                if title and company:
                    new_job = {"title": title, "company": company, "location": location, "visa": visa, "pay": pay, "desc": desc}
                    st.session_state.jobs.append(new_job)
                    st.success(t["post_success"])
                else:
                    st.error(t["post_error"])

# --- MENU: AI RESUME ---
elif selected == t["menu_ai"]:
    st.subheader(t["menu_ai"])
    st.write(t["ai_desc"])
    
    user_cv = st.text_area(t["menu_ai"], height=250, placeholder=t["ai_placeholder"])
    api_key = st.text_input("Google Gemini API Key (Optional):", type="password")
    
    if st.button(t["ai_btn"], type="primary"):
        if not api_key:
            st.warning(t["ai_warning"])
            st.markdown(f"""
            <div class="custom-card" style="background-color: #F0FDF4; border-color: #86EFAC;">
                <h4 style="color: #166534;">✨ AI Sample Review Output:</h4>
                <p><b>Original:</b> 저는 유학생입니다. 한국에서 알바를 하고 싶습니다. (Incorrect tone)</p>
                <p><b>Recommended:</b> 저는 끊임없이 도전하는 글로벌 인재로서, 귀사에서 가치를 발휘하고자 지원하였습니다. (Professional standard)</p>
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
                with st.spinner("AI is processing..."):
                    response = model.generate_content(prompt)
                    st.write("### AI Response:")
                    st.info(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

# --- NEW MENU: LANGUAGE & VISA EXAMS GUIDE ---
elif selected == t["menu_exams"]:
    st.subheader("📝 Korean Language Exams & Visa Integration Programs (TOPIK & KIIP)")
    st.write("Солонгос улсад суралцах, цагийн болон үндсэн ажил эрхлэх, мөн визээ сунгах/солиход (D-10, E-7, F-2, F-5) заавал шаардагддаг шалгалтуудын цогц мэдээлэл:")
    
    exam_tab1, exam_tab2, exam_tab3 = st.tabs(["📚 TOPIK (한국어능력시험)", "🤝 KIIP (사회통합프로그램)", "❓ Аль шалгалтыг нь өгөх вэ?"])
    
    with exam_tab1:
        st.markdown("""
        <div class="custom-card">
            <h3>Test of Proficiency in Korean (TOPIK)</h3>
            <p><b>Зорилго:</b> Солонгос улсын их дээд сургуульд элсэн орох, тэтгэлэг авах, цагийн ажлын зөвшөөрөл (시간제취업허가) авах болон визээ сунгахад (D-2-оос D-10 руу) голчлон ашиглагдана.</p>
            <div class="exam-header">📈 Шалгалтын бүтэц:</div>
            <ul>
                <li><b>TOPIK I (Анхан шат):</b> 1-2-р түвшин (Сонсох, Унших)</li>
                <li><b>TOPIK II (Дунд, Гүнзгий шат):</b> 3-6-р түвшин (Сонсох, Унших, Бичих)</li>
            </ul>
            <div class="exam-header">🔗 Албан ёсны вэбсайт болон бүртгүүлэх:</div>
            <p>Бүртгэл зөвхөн албан ёсны сайтаар онлайнаар явагддаг. Суудлын тоо хязгаартай тул бүртгэл эхлэх цагт шууд орох хэрэгтэй.</p>
            <a href="https://www.topik.go.kr" target="_blank"><button style="background-color: #4F46E5; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: bold;">TOPIK Вэбсайт руу зочлох</button></a>
        </div>
        """, unsafe_allow_html=True)
        
    with exam_tab2:
        st.markdown("""
        <div class="custom-card">
            <h3>Korea Immigration & Integration Program (KIIP - 사회통합プログラム)</h3>
            <p><b>Зорилго:</b> Солонгосын Хууль Зүйн Яамнаас зохион байгуулдаг бөгөөд урт хугацааны виз (F-2, F-5 резидент болон байнгын оршин суух виз) авахад, мөн E-7-4 (ур чадвартай ажилтан) визний оноо цуглуулахад асар өндөр давуу тал олгоно.</p>
            <div class="exam-header">⚙️ Хөтөлбөрийн бүтэц:</div>
            <p>Шалгуулагч эхлээд <b>Түвшин тогтоох шалгалт (사전평가)</b> өгч, онооноосоо хамаарч дараах шатуудаас суралцаж эхэлнэ:</p>
            <ul>
                <li>0-ээс 4-р шат: Солонгос хэл, соёл</li>
                <li>5-р шат: Солонгос орны тухай ойлголт (Нийгэм, Хууль, Түүх)</li>
            </ul>
            <div class="exam-header">🔗 Албан ёсны бүртгэл (Soci-Net):</div>
            <p>Уг програмд хамрагдахын тулд дараах хаягаар нэвтэрч бүртгүүлнэ үү:</p>
            <a href="https://www.socinet.go.kr" target="_blank"><button style="background-color: #06B6D4; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: bold;">Soci-Net Вэбсайт руу зочлох</button></a>
        </div>
        """, unsafe_allow_html=True)
        
    with exam_tab3:
        st.markdown("""
        <div class="custom-card">
            <h3>📊 Сонголт хийх зааварчилгаа</h3>
            <table style="width:100%; border-collapse: collapse; text-align: left;">
              <tr style="background-color: #f3f4f6; border-bottom: 2px solid #e5e7eb;">
                <th style="padding: 10px;">Шалгуур</th>
                <th style="padding: 10px;">TOPIK (한국어능력시험)</th>
                <th style="padding: 10px;">KIIP (사회통합프로그램)</th>
              </tr>
              <tr style="border-bottom: 1px solid #e5e7eb;">
                <td style="padding: 10px; font-weight: bold;">Гол зорилго</td>
                <td style="padding: 10px;">Сургууль, ажил, цагийн ажлын зөвшөөрөл</td>
                <td style="padding: 10px;">Урт хугацааны виз сунгалт, оршин суух зөвшөөрөл (F серийн визүүд)</td>
              </tr>
              <tr style="border-bottom: 1px solid #e5e7eb;">
                <td style="padding: 10px; font-weight: bold;">Хүчинтэй хугацаа</td>
                <td style="padding: 10px;">2 жил хүчинтэй</td>
                <td style="padding: 10px;">Хүчинтэй хугацаа байхгүй (Төгссөн бол насан туршдаа хүчинтэй)</td>
              </tr>
              <tr style="border-bottom: 1px solid #e5e7eb;">
                <td style="padding: 10px; font-weight: bold;">Давуу тал</td>
                <td style="padding: 10px;">Гадаад орнуудад ч хүчинтэй</td>
                <td style="padding: 10px;">Визний оноо маш сайн цуглуулна, сургалт нь үнэ төлбөргүй</td>
              </tr>
            </table>
            <br>
            <p>💡 <b>Мэргэжлийн зөвлөгөө:</b> Хэрэв та солонгос улсад 2-оос дээш жил сурч, цаашдаа суурьшин ажиллахаар төлөвлөж байгаа бол <b>KIIP (사회통합프로그램)</b> хөтөлбөрийг эртнээс эхлүүлэхийг зөвлөж байна. Энэ нь таны виз сунгалтын хамгийн том зэвсэг болно!</p>
        </div>
        """, unsafe_allow_html=True)

# --- MENU: TRAINING ---
elif selected == t["menu_training"]:
    st.subheader(t["menu_training"])
    courses = [
        {"title": "TOPIK Prep Masterclass", "duration": "4 Weeks", "level": "Intermediate to Advanced", "desc": "Effective strategies to reach the required TOPIK score for Korean corporates.", "icon": "📚"},
        {"title": "Corporate Internship Preparation", "duration": "2 Weeks", "level": "All Levels", "desc": "Comprehensive training from drafting professional cover letters to live interview simulations.", "icon": "👔"},
        {"title": "Visa Transition & Employment Roadmap", "duration": "3 Seminars", "level": "Senior Students", "desc": "Guidance on converting D-2 visas to D-10 job seeker and E-7 work visas.", "icon": "✈️"}
    ]
    for c in courses:
        col_icon, col_content = st.columns([1, 9])
        with col_icon:
            st.markdown(f"<h1 style='text-align: center; margin-top: 15px;'>{c['icon']}</h1>", unsafe_allow_html=True)
        with col_content:
            st.markdown(f"""
            <div class="custom-card">
                <span class="badge" style="background-color: #EEF2F6; color: #4F46E5;">⏱️ {c['duration']}</span>
                <span class="badge" style="background-color: #ECFDF5; color: #059669;">📶 {c['level']}</span>
                <h4 style="margin-top: 10px;">{c['title']}</h4>
                <p style="color: #4B5563; font-size: 14px;">{c['desc']}</p>
                <button style="background-color: #4F46E5; color: white; border: none; padding: 8px 16px; border-radius: 8px; cursor: pointer;">{t['btn_register']}</button>
            </div>
            """, unsafe_allow_html=True)

# --- MENU: TIPS & STORIES ---
elif selected == t["menu_tips"]:
    st.subheader(t["menu_tips"])
    st.markdown(f"""
    <div class="custom-card" style="background-color: #FFFBEB; border-color: #FDE68A;">
        <h4 style="color: #B45309;">💡 Visa Guide</h4>
        <p>{t['visa_alert']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    stories = [
        {"name": "Anudari B. (D-2)", "title": "On-Campus Office Assistant Experience", "content": "I worked at my university office. It didn't require immigration pre-clearance back then, making it extremely convenient. Great way to improve Korean conversational skills!"},
        {"name": "Temuulen T. (E-7)", "title": "From Intern to Full-time Employee", "content": "I started as an intern on my D-10 visa, and after proving myself, the company sponsored my E-7 visa. Adaptation and soft skills are just as important as technical skills."}
    ]
    for s in stories:
        st.markdown(f"""
        <div class="custom-card">
            <h5><b>{s['title']}</b></h5>
            <p style="font-size: 13px; color: #9CA3AF;">Posted by: {s['name']}</p>
            <p style="color: #374151; font-size: 14px;">"{s['content']}"</p>
        </div>
        """, unsafe_allow_html=True)