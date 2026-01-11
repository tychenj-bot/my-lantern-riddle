import streamlit as st
import random
import time

# 設定網頁標題與風格
st.set_page_config(page_title="TXT 追星鐵粉大作戰", page_icon="💙")

# 自定義 TXT 專屬 CSS 風格 (水藍色主題)
st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    .stButton>button { background-color: #00A6E3; color: white; border-radius: 10px; }
    .stProgress > div > div > div > div { background-color: #00A6E3; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. 完整 90 題校訂題庫 ---
if 'game_initialized' not in st.session_state:
    raw_levels = {
        1: {
            "name": "🌱 第一關：MOA 初級生 (基本資料)",
            "pool": [
                {"q": "TXT 官方粉絲名 MOA 的全稱是？", "a": "Moments Of Alwaysness", "options": ["Moments Of Alwaysness", "Music Of Alwaysness", "Memory Of Artist", "Moment Of ACE"], "hint": "這代表 TXT 與粉絲永遠在一起"},
                {"q": "TXT 的大哥 YEONJUN 的代表動物是？", "a": "狐狸", "options": ["兔子", "狐狸", "熊", "松鼠"], "hint": "沙漠狐狸"},
                {"q": "TXT 的隊長 SOOBIN 的代表動物是？", "a": "兔子", "options": ["兔子", "狐狸", "松鼠", "企鵝"], "hint": "長耳朵代表"},
                {"q": "TXT 的出道日期是哪一天？", "a": "2019年3月4日", "options": ["2018年3月4日", "2019年3月4日", "2019年4月3日", "2020年3月4日"], "hint": "春季出道"},
                {"q": "TXT 隸屬於哪一家經紀公司？", "a": "BIGHIT MUSIC", "options": ["SM", "YG", "JYP", "BIGHIT MUSIC"], "hint": "BTS 的師弟團"},
                {"q": "成員 BEOMGYU 來自哪個城市？", "a": "大邱", "options": ["首爾", "大邱", "釜山", "光州"], "hint": "有著可愛的方言"},
                {"q": "HUENING KAI 的爸爸是什麼國籍？", "a": "美國", "options": ["德國", "美國", "巴西", "韓國"], "hint": "國籍為美國"},
                {"q": "成員 TAEHYUN 最喜歡的運動項目是？", "a": "拳擊", "options": ["拳擊", "籃球", "足球", "游泳"], "hint": "他在練習生時期很專注這項運動"},
                {"q": "TXT 的官方手燈名稱是？", "a": "MOABONG", "options": ["TXTBONG", "MOABONG", "STARBONG", "BLUEBONG"], "hint": "粉絲名+棒"},
                {"q": "TXT 出道曲《CROWN》中，成員頭上長了什麼？", "a": "角", "options": ["角", "翅膀", "光環", "尾巴"], "hint": "成長的陣痛"},
                {"q": "TXT 成員中誰的身高最高 (185cm)？", "a": "SOOBIN", "options": ["YEONJUN", "SOOBIN", "HUENING KAI", "BEOMGYU"], "hint": "長腿隊長"},
                {"q": "哪位成員出生於夏威夷？", "a": "HUENING KAI", "options": ["YEONJUN", "SOOBIN", "HUENING KAI", "TAEHYUN"], "hint": "忙內"},
                {"q": "TXT 粉絲名稱 MOA 公布的年份是？", "a": "2019年", "options": ["2018年", "2019年", "2020年", "2021年"], "hint": "出道同年"},
                {"q": "成員 SOOBIN 唯一的寵物刺蝟叫什麼？", "a": "Odi", "options": ["Odi", "Bokshil", "Doddok", "Pudu"], "hint": "名字很短"},
                {"q": "YEONJUN 在 BIGHIT 練習時間大約多久？", "a": "5年", "options": ["1年", "3年", "5年", "7年"], "hint": "練習最久的成員"},
                {"q": "哪首 MV 中出現了「旋轉木馬」與「夕陽」？", "a": "Blue Hour", "options": ["Blue Hour", "Crown", "Run Away", "Magic"], "hint": "粉色與橘色調"},
                {"q": "成員 BEOMGYU 的代表動物是？", "a": "熊", "options": ["熊", "松鼠", "兔子", "狐狸"], "hint": "也是小蝴蝶"},
                {"q": "TAEHYUN 的代表動物是？", "a": "松鼠", "options": ["松鼠", "兔子", "企鵝", "貓"], "hint": "大大的眼睛"},
                {"q": "HUENING KAI 的代表動物是？", "a": "企鵝", "options": ["企鵝", "松鼠", "兔子", "熊"], "hint": "也有獨角獸形象"},
                {"q": "TXT 的全稱是什麼？", "a": "TOMORROW X TOGETHER", "options": ["TOMORROW X TOGETHER", "TEAM X TRUST", "TEN X TOGETHER", "TIME X TODAY"], "hint": "明天與彼此"},
                {"q": "TXT 第一個獲得一位的節目是？", "a": "The Show", "options": ["M Countdown", "Music Bank", "The Show", "Inkigayo"], "hint": "出道僅 8 天"},
                {"q": "哪首歌曲提到頭上長了角？", "a": "CROWN", "options": ["CROWN", "Blue Hour", "Run Away", "Sugar Rush Ride"], "hint": "出道曲"},
                {"q": "TXT 中唯一一位 1999 年生的是？", "a": "YEONJUN", "options": ["YEONJUN", "SOOBIN", "BEOMGYU", "TAEHYUN"], "hint": "大哥"},
                {"q": "TXT 中誰是 2000 年生的隊長？", "a": "SOOBIN", "options": ["YEONJUN", "SOOBIN", "BEOMGYU", "TAEHYUN"], "hint": "唯一 00 年生"},
                {"q": "BEOMGYU 的生日月份是？", "a": "3月", "options": ["3月", "5月", "8月", "12月"], "hint": "3月13日"},
                {"q": "TAEHYUN 最擅長的技能除了唱歌還有？", "a": "魔術", "options": ["魔術", "烹飪", "畫畫", "剪輯"], "hint": "他小時候夢想是魔術師"},
                {"q": "HUENING KAI 收集最多的是？", "a": "絨毛娃娃", "options": ["絨毛娃娃", "帽子", "鞋子", "香水"], "hint": "床上一大堆"},
                {"q": "成員 YEONJUN 最喜歡的食物是？", "a": "拉麵", "options": ["拉麵", "沙拉", "麵包", "苦瓜"], "hint": "他很愛吃麵"},
                {"q": "TXT 手燈按鈕上的標誌形狀是？", "a": "十字形", "options": ["星形", "十字形", "圓形", "方形"], "hint": "團體標誌"},
                {"q": "TXT 哪位成員是 A 型血？", "a": "TAEHYUN", "options": ["TAEHYUN", "SOOBIN", "BEOMGYU", "YEONJUN"], "hint": "邏輯強性格謹慎"}
            ]
        },
        2: {
            "name": "🔥 第二關：MOA 進階班 (綜藝與作品)",
            "pool": [
                {"q": "哪首歌的編舞出現了「狗叫聲」動作？", "a": "Cat & Dog", "options": ["Crown", "Cat & Dog", "PUMA", "Blue Hour"], "hint": "汪汪汪！"},
                {"q": "TXT 第一個團綜名稱是？", "a": "ONE DREAM.TXT", "options": ["ONE DREAM.TXT", "TO DO", "TXT LOG", "TALK X TODAY"], "hint": "紀錄美國行"},
                {"q": "SOOBIN 曾擔任過哪個節目的 MC？", "a": "Music Bank", "options": ["M Countdown", "Music Bank", "Inkigayo", "Show Champion"], "hint": "與 Arin 搭配"},
                {"q": "YEONJUN 曾經在 BIGHIT 獲得什麼稱號？", "a": "傳奇練習生", "options": ["傳奇練習生", "舞蹈天才", "全能忙內", "IT Boy"], "hint": "月評第一名"},
                {"q": "歌曲《0X1=LOVESONG》的風格主要是？", "a": "搖滾", "options": ["搖滾", "雷鬼", "爵士", "純鋼琴"], "hint": "熱血嘶吼感"},
                {"q": "BEOMGYU 曾自稱如果他是 MOA 本命會是？", "a": "BEOMGYU", "options": ["SOOBIN", "YEONJUN", "BEOMGYU", "TAEHYUN"], "hint": "自信滿分"},
                {"q": "哪首是 TXT 的首支英文單曲？", "a": "Magic", "options": ["Magic", "Cat & Dog", "Blue Hour", "Anti-Romantic"], "hint": "It's like magic!"},
                {"q": "在《TO DO》中，誰被稱為「遊戲破壞者」？", "a": "BEOMGYU", "options": ["SOOBIN", "YEONJUN", "BEOMGYU", "TAEHYUN"], "hint": "調皮搗蛋第一名"},
                {"q": "哪位成員參與了《Maze in the Mirror》製作？", "a": "全體成員", "options": ["全體成員", "BEOMGYU", "YEONJUN", "TAEHYUN"], "hint": "自創曲"},
                {"q": "TXT 首個進入 Billboard 200 前五名的專輯？", "a": "FREEZE", "options": ["STAR", "MAGIC", "FREEZE", "TEMPTATION"], "hint": "混沌章節"},
                {"q": "HUENING KAI 領養的綠色兔子娃娃叫什麼？", "a": "Tobin", "options": ["Tobin", "Molang", "Pudu", "Doddok"], "hint": "跟 Soobin 相關"},
                {"q": "哪首歌 MV 在塞班島拍攝？", "a": "LOVESONG (JP Ver.)", "options": ["LOVESONG (JP Ver.)", "Blue Hour", "Magic", "Crown"], "hint": "風景優美"},
                {"q": "哪位成員最熱愛「草莓歐蕾」？", "a": "BEOMGYU", "options": ["BEOMGYU", "SOOBIN", "YEONJUN", "TAEHYUN"], "hint": "他曾多次提到"},
                {"q": "YEONJUN 的英文名字是？", "a": "Daniel", "options": ["Daniel", "Kevin", "Leo", "Jason"], "hint": "小時候去過美國"},
                {"q": "《Blue Hour》韓文歌名中的數字是？", "a": "5時53分", "options": ["5時53分", "6時30分", "4時15分", "7時21分"], "hint": "非常著名的數字"},
                {"q": "TAEHYUN 被稱為「人生幾周目」？", "a": "2周目", "options": ["2周目", "3周目", "1周目", "5周目"], "hint": "因為很成熟"},
                {"q": "TXT 成員曾全體客串過什麼？", "a": "韓劇 Live On", "options": ["韓劇 Live On", "動漫", "電影", "紀錄片"], "hint": "Yeonjun 有較多戲份"},
                {"q": "HUENING KAI 擅長的樂器除了鋼琴還有？", "a": "吉他", "options": ["吉他", "爵士鼓", "小提琴", "笛子"], "hint": "音樂世家"},
                {"q": "哪首歌在 TikTok 爆紅吸引大量非 MOA 聽眾？", "a": "Anti-Romantic", "options": ["Anti-Romantic", "Crown", "Blue Hour", "Run Away"], "hint": "非浪漫"},
                {"q": "YEONJUN 與誰是「巧克力派」好友？", "a": "HUENING KAI", "options": ["HUENING KAI", "SOOBIN", "BEOMGYU", "TAEHYUN"], "hint": "薄巧派"},
                {"q": "哪首歌的舞蹈有「耳朵」的動作？", "a": "Cat & Dog", "options": ["Cat & Dog", "Crown", "Blue Hour", "Run Away"], "hint": "動物系列"},
                {"q": "成員 BEOMGYU 練習生時期常躲在哪裡哭？", "a": "洗手間", "options": ["洗手間", "天台", "操場", "宿舍"], "hint": "辛酸史"},
                {"q": "TXT 成員中誰最討厭吃香菜？", "a": "YEONJUN", "options": ["YEONJUN", "SOOBIN", "BEOMGYU", "TAEHYUN"], "hint": "他在直播提過"},
                {"q": "TAEHYUN 的 MBTI 傾向是？", "a": "T", "options": ["T", "F", "P", "A"], "hint": "理性邏輯王"},
                {"q": "在《TO DO》廚房特輯中誰被封為大廚？", "a": "TAEHYUN", "options": ["TAEHYUN", "YEONJUN", "SOOBIN", "BEOMGYU"], "hint": "穩定發揮"},
                {"q": "TXT 與 Coi Leray 合作的歌曲？", "a": "Happy Fools", "options": ["Happy Fools", "Magic", "Sugar Rush Ride", "Tinnitus"], "hint": "誘惑章節"},
                {"q": "哪位成員是 SHINee 泰民的粉絲？", "a": "TAEHYUN", "options": ["TAEHYUN", "SOOBIN", "YEONJUN", "BEOMGYU"], "hint": "泰民粉絲"},
                {"q": "成員 SOOBIN 最愛的飲品？", "a": "巧克力牛奶", "options": ["巧克力牛奶", "美式
