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
                {"q": "成員 SOOBIN 最愛的飲品？", "a": "巧克力牛奶", "options": ["巧克力牛奶", "美式咖啡", "綠茶", "可樂"], "hint": "甜甜的"},
                {"q": "TXT 哪首歌曲有九又四分之三月台概念？", "a": "Run Away", "options": ["Run Away", "Crown", "Magic", "PUMA"], "hint": "哈利波特概念"},
                {"q": "哪位成員是團內公認的模仿王？", "a": "BEOMGYU", "options": ["BEOMGYU", "YEONJUN", "SOOBIN", "HUENING KAI"], "hint": "模仿老闆最像"}
            ]
        },
        3: {
            "name": "🏆 第三關：TXT 鐵粉大師 (細節考驗)",
            "pool": [
                {"q": "SOOBIN 領養 Odi 的年份？", "a": "2021年", "options": ["2019年", "2020年", "2021年", "2022年"], "hint": "MOA 熟知的年份"},
                {"q": "TAEHYUN 的視力曾經提過是多少？", "a": "1.5", "options": ["1.0", "1.5", "0.5", "2.0"], "hint": "非常好"},
                {"q": "YEONJUN 出道預告公開日期？", "a": "2019年1月11日", "options": ["2019年1月11日", "2019年1月10日", "2019年3月4日", "2019年2月1日"], "hint": "第一個成員"},
                {"q": "SOOBIN 出道初期官方體重設定？", "a": "67kg", "options": ["60kg", "67kg", "72kg", "75kg"], "hint": "185cm 的他很瘦"},
                {"q": "哪次巡演名稱是 ACT: LOVE SICK？", "a": "2022年首場巡演", "options": ["2022年首場巡演", "2023年巡演", "2024年巡演", "2019年秀"], "hint": "LOVE SICK"},
                {"q": "YEONJUN 的手掌大約多長？", "a": "19cm", "options": ["15cm", "17cm", "19cm", "21cm"], "hint": "大手"},
                {"q": "HUENING KAI 最愛的娃娃品牌？", "a": "Molang", "options": ["Molang", "Disney", "Sanrio", "BT21"], "hint": "白色兔子"},
                {"q": "哪位成員最怕酪梨的口感？", "a": "SOOBIN", "options": ["SOOBIN", "YEONJUN", "BEOMGYU", "TAEHYUN"], "hint": "像肥皂"},
                {"q": "TXT 在 Lollapalooza 主舞台領銜嘉賓年份？", "a": "2023年", "options": ["2021年", "2022年", "2023年", "2024年"], "hint": "歷史紀錄"},
                {"q": "SOOBIN 的生日月份與日期？", "a": "12月5日", "options": ["12月5日", "12月4日", "12月6日", "12月10日"], "hint": "射手座"},
                {"q": "BEOMGYU 最討厭吃的水果 (他覺得是蔬菜)？", "a": "番茄", "options": ["番茄", "西瓜", "香蕉", "蘋果"], "hint": "紅紅的"},
                {"q": "YEONJUN BIGHIT 面試曲？", "a": "Boy In Luv", "options": ["Boy In Luv", "Baby", "Rainism", "Growl"], "hint": "BTS 前輩歌"},
                {"q": "TXT 第一張日語專輯名稱？", "a": "STILL DREAMING", "options": ["STILL DREAMING", "SWEET", "DRAMA", "MAGIC"], "hint": "還在夢中"},
                {"q": "哪首歌曲 MV 出現「火海」與「操場」？", "a": "Run Away", "options": ["Run Away", "Crown", "Blue Hour", "Magic Island"], "hint": "九又四分之三"},
                {"q": "HUENING KAI 在中國居住過大約多久？", "a": "7年", "options": ["2年", "5年", "7年", "10年"], "hint": "小時候"},
                {"q": "BEOMGYU 被挖掘的地點？", "a": "大邱街頭", "options": ["大邱街頭", "首爾地鐵", "學校", "海邊"], "hint": "特地去找他"},
                {"q": "哪首歌在 2024 年破 2 億播放？", "a": "Sugar Rush Ride", "options": ["Sugar Rush Ride", "Crown", "Blue Hour", "Run Away"], "hint": "性感風"},
                {"q": "哪位成員被稱為遊戲黑洞？", "a": "SOOBIN", "options": ["SOOBIN", "YEONJUN", "TAEHYUN", "BEOMGYU"], "hint": "努力但手氣差"},
                {"q": "成員中誰的身高是 177cm？", "a": "TAEHYUN", "options": ["TAEHYUN", "BEOMGYU", "SOOBIN", "YEONJUN"], "hint": "隊內最小隻"},
                {"q": "TXT 哪位成員最怕鬼且反應最大？", "a": "BEOMGYU", "options": ["BEOMGYU", "YEONJUN", "TAEHYUN", "HUENING KAI"], "hint": "反應超搞笑"},
                {"q": "TXTDone 第一張預告照文字？", "a": "What do you do?", "options": ["What do you do?", "Who am I?", "Hello Tomorrow", "Together"], "hint": "問句"},
                {"q": "成員 YEONJUN 的手掌寬度大約？", "a": "19cm", "options": ["15cm", "17cm", "19cm", "21cm"], "hint": "重複考驗"},
                {"q": "哪位成員最喜歡薄荷巧克力？", "a": "YEONJUN/HUENING", "options": ["YEONJUN/HUENING", "SOOBIN", "BEOMGYU", "TAEHYUN"], "hint": "薄巧戰士"},
                {"q": "SOOBIN 的酒量大約？", "a": "半瓶燒酒", "options": ["半瓶燒酒", "三瓶燒酒", "一杯醉", "十瓶"], "hint": "自爆過"},
                {"q": "哪位成員擅長拳擊？", "a": "TAEHYUN", "options": ["TAEHYUN", "YEONJUN", "SOOBIN", "BEOMGYU"], "hint": "練習生時期"},
                {"q": "TXT 首個大賞獎項來自？", "a": "The Fact Music Awards", "options": ["The Fact", "MAMA", "MMA", "Golden Disc"], "hint": "2023大突破"},
                {"q": "哪位成員小時候夢想是魔術師？", "a": "TAEHYUN", "options": ["TAEHYUN", "YEONJUN", "SOOBIN", "BEOMGYU"], "hint": "魔術"},
                {"q": "哪位成員英文名叫 Daniel？", "a": "HUENING KAI", "options": ["HUENING KAI", "YEONJUN", "SOOBIN", "BEOMGYU"], "hint": "Daniel"},
                {"q": "成員中誰是 01 年生？", "a": "BEOMGYU", "options": ["BEOMGYU", "SOOBIN", "YEONJUN", "TAEHYUN"], "hint": "01"},
                {"q": "TXT 出道曲韓文歌名？", "a": "有一天頭上長了角", "options": ["有一天頭上長了角", "皇冠", "星星", "魔法"], "hint": "長了角"}
            ]
        }
    }

    # 初始化每一關的題目
    st.session_state.levels = {}
    for i in [1, 2, 3]:
        shuffled_pool = random.sample(raw_levels[i]["pool"], 30)
        for item in shuffled_pool:
            random.shuffle(item["options"])
        st.session_state.levels[i] = {
            "name": raw_levels[i]["name"],
            "questions": shuffled_pool
        }

    st.session_state.current_level = 1
    st.session_state.correct_in_level = 0
    st.session_state.q_pool_idx = 0
    st.session_state.total_score = 0
    st.session_state.game_finished = False
    st.session_state.game_initialized = True

# --- 2. 遊戲介面 ---
st.title("💙 TXT 追星鐵粉大作戰 💛")

if not st.session_state.game_finished:
    lv = st.session_state.current_level
    current_lv_data = st.session_state.levels[lv]
    
    st.subheader(f"當前進度：{current_lv_data['name']}")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write(f"本關答對：**{st.session_state.correct_in_level} / 3**")
    with col_b:
        st.write(f"剩餘挑戰：**{30 - st.session_state.q_pool_idx}** 題")
    
    st.progress(st.session_state.correct_in_level / 3)

    if st.session_state.q_pool_idx < 30:
        current_q = current_lv_data["questions"][st.session_state.q_pool_idx]

        with st.container(border=True):
            st.markdown(f"### Q: {current_q['q']}")
            
            # 選擇題按鈕
            cols = st.columns(2)
            for i, option in enumerate(current_q["options"]):
                with cols[i % 2]:
                    if st.button(option, key=f"btn_{lv}_{st.session_state.q_pool_idx}_{i}", use_container_width=True):
                        if option == current_q["a"]:
                            st.success("✨ 答對了！不愧是 MOA！")
                            st.session_state.correct_in_level += 1
                            st.session_state.total_score += 1
                        else:
                            st.error(f"❌ 答錯了！正確答案是「{current_q['a']}」")
                        
                        time.sleep(1.2)
                        st.session_state.q_pool_idx += 1
                        
                        if st.session_state.correct_in_level >= 3:
                            if lv < 3:
                                st.balloons()
                                if lv == 2: st.snow()
                                st.session_state.current_level += 1
                                st.session_state.correct_in_level = 0
                                st.session_state.q_pool_idx = 0
                                st.toast(f"🚀 通關！即將挑戰難度升級！")
                            else:
                                st.session_state.game_finished = True
                        st.rerun()
            
            if st.button("💡 獲取 MOA 專屬提示"):
                st.info(f"小提示：{current_q['hint']}")
    else:
        st.error("😭 30 題機會用完了，看來還要再多看 TO DO 喔！")
        if st.button("重新挑戰本關"):
            st.session_state.correct_in_level = 0
            st.session_state.q_pool_idx = 0
            random.shuffle(st.session_state.levels[lv]["questions"])
            st.rerun()

else:
    # --- 3. 終極通關 ---
    st.balloons()
    st.snow()
    st.markdown("<h1 style='text-align: center; color: #00A6E3;'>🏆 恭喜成為【TXT 傳奇級 MOA】！</h1>", unsafe_allow_html=True)
    st.write(f"在三場挑戰中，你總共拿下了 {st.session_state.total_score} 分！")
    
    # PPULBATU 慶祝 GIF 💙
    st.image("https://media.tenor.com/Co3t0_2Z8SEAAAAd/ppulbatu-txt.gif", caption="PPULBATU 全員為傳奇級 MOA 慶祝！✨", use_container_width=True)
    
    if st.button("重新開始 MOA 知識挑戰"):
        del st.session_state['game_initialized']
        st.rerun()

# --- 4. 側邊欄 ---
with st.sidebar:
    st.write("### 💙 Tomorrow X Together")
    st.write("這是一款專為 MOA 設計的挑戰。")
    st.write("1. 難度從入門、進階到大師級。")
    st.write("2. 每關隨機 30 題選題。")
    st.write("3. 答錯直接換下一題，對 3 題即通關。")
