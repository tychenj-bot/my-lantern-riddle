import streamlit as st
import random
import time

# 設定網頁標題與風格
st.set_page_config(page_title="TXT 追星鐵粉大作戰", page_icon="💙")

# --- 1. TXT 鐵粉題庫 (混合 3 關) ---
if 'game_initialized' not in st.session_state:
    raw_levels = {
        1: {
            "name": "🌱 第一關：MOA 初級生 (簡單)",
            "pool": [
                {"q": "TXT 的出道日期是哪一天？", "a": "2019年3月4日", "options": ["2018年3月4日", "2019年3月4日", "2019年4月3日", "2020年3月4日"], "hint": "這是在 BIGHIT 公布的正式日期"},
                {"q": "TXT 的官方粉絲名稱是什麼？", "a": "MOA", "options": ["MOA", "ARMY", "STAY", "ONCE"], "hint": "意為 Moments Of Alwaysness"},
                {"q": "TXT 的出道曲名稱是什麼？", "a": "CROWN (有一天頭上長了角)", "options": ["CROWN (有一天頭上長了角)", "Blue Hour", "Sugar Rush Ride", "Run Away"], "hint": "歌詞提到頭上長了角"},
                {"q": "TXT 的隊長是哪一位成員？", "a": "SOOBIN", "options": ["YEONJUN", "SOOBIN", "BEOMGYU", "TAEHYUN"], "hint": "他是溫柔的兔子代表"},
                {"q": "TXT 成員中，誰被稱為「四代首位 IT Boy」？", "a": "YEONJUN", "options": ["YEONJUN", "BEOMGYU", "TAEHYUN", "HUENING KAI"], "hint": "是大哥且時尚感極強"},
                {"q": "TXT 隸屬於哪一家經紀公司？", "a": "BIGHIT MUSIC", "options": ["SM", "YG", "JYP", "BIGHIT MUSIC"], "hint": "BTS 的師弟團"},
                {"q": "成員 BEOMGYU 來自韓國哪個城市？", "a": "大邱", "options": ["首爾", "釜山", "大邱", "仁川"], "hint": "這也是許多偶像的故鄉"},
                {"q": "成員 HUENING KAI 在隊內擔任的角色包含？", "a": "忙內", "options": ["忙內", "隊長", "大哥", "主舞"], "hint": "他是家裡的老么，也是隊內最小的"},
                {"q": "TXT 的全稱是什麼？", "a": "TOMORROW X TOGETHER", "options": ["TOMORROW X TOGETHER", "TEAM X TRUST", "TEN X TOGETHER", "TIME X TODAY"], "hint": "明天與彼此在一起"},
                {"q": "TXT 的官方手燈名稱是？", "a": "MOABONG", "options": ["TXTBONG", "MOABONG", "STARBONG", "BLUEBONG"], "hint": "粉絲名+棒"}
            ]
        },
        2: {
            "name": "🔥 第二關：MOA 進階班 (中等)",
            "pool": [
                {"q": "哪一位成員曾在 Music Bank 擔任過固定 MC？", "a": "SOOBIN", "options": ["SOOBIN", "YEONJUN", "BEOMGYU", "TAEHYUN"], "hint": "與 Oh My Girl 的 Arin 合作"},
                {"q": "TXT 的第一張正規專輯名稱是？", "a": "The Dream Chapter: MAGIC", "options": ["The Dream Chapter: STAR", "The Dream Chapter: MAGIC", "minisode 1 : Blue Hour", "The Chaos Chapter: FREEZE"], "hint": "包含歌曲 Run Away"},
                {"q": "哪首歌曲讓 TXT 在美國 Lollapalooza 音樂節上引起巨大迴響？", "a": "Good Boy Gone Bad", "options": ["Crown", "Blue Hour", "Good Boy Gone Bad", "Sugar Rush Ride"], "hint": "展現了強烈的搖滾風格"},
                {"q": "成員 TAEHYUN 曾表示自己小時候的夢想是？", "a": "魔術師", "options": ["魔術師", "拳擊手", "醫生", "科學家"], "hint": "他現在也很擅長變魔術"},
                {"q": "成員 YEONJUN 曾經在 Cube 娛樂當過練習生嗎？", "a": "是的", "options": ["是的", "不是", "他只在 BIGHIT", "他是 JYP 的"], "hint": "他是 BIGHIT 的傳奇練習生，但之前有過經驗"},
                {"q": "TXT 的團體綜藝節目名稱是？", "a": "TO DO X TXT", "options": ["GOING TXT", "TO DO X TXT", "TXT LOG", "RUN TXT"], "hint": "每週一更新的搞笑綜藝"},
                {"q": "HUENING KAI 的姐姐 Lea 曾是哪個女團的成員？", "a": "VIVA", "options": ["VIVA", "Kep1er", "IVE", "NewJeans"], "hint": "Kep1er 的休寧巴伊葉是他的妹妹"},
                {"q": "歌曲《Blue Hour》的韓文歌名是什麼？", "a": "在 5 時 53 分的夜空發現的你跟我", "options": ["在 5 時 53 分的夜空發現的你跟我", "等待你的天空", "藍色的時光", "在海邊相見"], "hint": "歌名非常長"},
                {"q": "成員 BEOMGYU 最喜歡的樂器是？", "a": "吉他", "options": ["吉他", "鋼琴", "爵士鼓", "小提琴"], "hint": "他出道前曾組過樂隊"},
                {"q": "哪一位成員被稱為「人生二周目」，意思是非常成熟？", "a": "TAEHYUN", "options": ["TAEHYUN", "SOOBIN", "YEONJUN", "BEOMGYU"], "hint": "名言製造機，說話很有邏輯"}
            ]
        },
        3: {
            "name": "🏆 第三關：TXT 鐵粉大師 (困難)",
            "pool": [
                {"q": "SOOBIN 的寵物刺蝟名字叫做什麼？", "a": "Odi", "options": ["Odi", "Bokshil", "Doddok", "Pudu"], "hint": "名字很短很可愛"},
                {"q": "YEONJUN 曾在《人氣歌謠》表演的傳奇 Solo 舞台曲目是？", "a": "Water", "options": ["Water", "Guilty", "Smoke", "Hype Boy"], "hint": "挑戰了 Tyla 的熱門歌曲"},
                {"q": "TXT 在 2023 年發行的首張日語正規專輯名稱是？", "a": "SWEET", "options": ["STILL DREAMING", "CHAOTIC WONDERLAND", "SWEET", "DRAMA"], "hint": "封面非常粉嫩"},
                {"q": "在《TO DO》中，哪位成員常被稱為「遊戲黑洞」？", "a": "SOOBIN", "options": ["SOOBIN", "YEONJUN", "TAEHYUN", "BEOMGYU"], "hint": "雖然很努力但運氣或技巧常出錯"},
                {"q": "TAEHYUN 的官方身高是多少？", "a": "177cm", "options": ["175cm", "177cm", "179cm", "181cm"], "hint": "他是隊內最矮的，但在其他團算高"},
                {"q": "TXT 在哪一年首次登上《滾石》雜誌封面？", "a": "2021年", "options": ["2019年", "2020年", "2021年", "2022年"], "hint": "與 The Chaos Chapter 宣傳期相關"},
                {"q": "歌曲《Cat & Dog》的英文版歌詞中，第一句是誰唱的？", "a": "YEONJUN", "options": ["YEONJUN", "SOOBIN", "TAEHYUN", "HUENING KAI"], "hint": "這首歌的饒舌部分很有名"},
                {"q": "BEOMGYU 曾經在練習生時期，因為練習太累而躲到哪裡大哭？", "a": "洗手間", "options": ["洗手間", "天台", "公園", "宿舍衣櫃"], "hint": "是偶像練習生常見的辛酸史"},
                {"q": "TXT 哪位成員最怕恐怖的東西，但在節目中常被嚇？", "a": "BEOMGYU", "options": ["BEOMGYU", "TAEHYUN", "HUENING KAI", "YEONJUN"], "hint": "他的反應非常大且搞笑"},
                {"q": "TXT 第一個獲得 1 億播放量的 MV 是哪一首？", "a": "CROWN", "options": ["CROWN", "Blue Hour", "Run Away", "Cat & Dog"], "hint": "出道即巔峰的紀錄"},
            ]
        }
    }

    # 每個關卡隨機選題 (目前範例各10題，你可以自行擴充至30題)
    st.session_state.levels = {}
    for i in [1, 2, 3]:
        shuffled_pool = random.sample(raw_levels[i]["pool"], len(raw_levels[i]["pool"]))
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
st.title("💙 TXT 追星鐵粉知識大作戰 💛")

if not st.session_state.game_finished:
    lv = st.session_state.current_level
    current_lv_data = st.session_state.levels[lv]
    
    st.subheader(f"當前進度：{current_lv_data['name']}")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write(f"本關答對：**{st.session_state.correct_in_level} / 3**")
    with col_b:
        st.write(f"剩餘題目：**{len(current_lv_data['questions']) - st.session_state.q_pool_idx}**")
    
    st.progress(st.session_state.correct_in_level / 3)

    if st.session_state.q_pool_idx < len(current_lv_data['questions']):
        current_q = current_lv_data["questions"][st.session_state.q_pool_idx]

        with st.container(border=True):
            st.markdown(f"### Q{st.session_state.q_pool_idx + 1}: {current_q['q']}")
            
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
                                st.toast(f"🚀 通關！進入更高階挑戰")
                            else:
                                st.session_state.game_finished = True
                        st.rerun()
            
            if st.button("💡 獲取 MOA 專屬提示"):
                st.info(f"小提示：{current_q['hint']}")
    else:
        st.error("😭 本關題目用完了，答對數不足 3 題... 看來你還不夠鐵！")
        if st.button("重新挑战本關"):
            st.session_state.correct_in_level = 0
            st.session_state.q_pool_idx = 0
            random.shuffle(st.session_state.levels[lv]["questions"])
            st.rerun()

else:
    # --- 3. 通關畫面 (啦啦隊) ---
    st.balloons()
    st.snow()
    st.markdown("<h1 style='text-align: center; color: #00A6E3;'>🏆 恭喜成為【TXT 傳奇級 MOA】！</h1>", unsafe_allow_html=True)
    st.write(f"你在這場知識大作戰中，總共答對了 {st.session_state.total_score} 題！")
    
    # 啦啦隊 GIF
    st.image("https://media.giphy.com/media/l41lYCDgxP665gjVm/giphy.gif", caption="啦啦隊為你的鐵粉實力尖叫喝采！📣")
    
    if st.button("重新開始知識挑戰"):
        del st.session_state['game_initialized']
        st.rerun()

# --- 4. 側邊欄 ---
with st.sidebar:
    st.write("### 💙 Tomorrow X Together")
    st.write("這是一款專為 MOA 設計的挑戰。")
    st.write("1. 難度從入門、進階到大師級。")
    st.write("2. 每關隨機 30 題選題。")
    st.write("3. 答錯直接換下一題，對 3 題即通關。")
    st.divider()
    st.write("祝你在 TXT 的音樂世界裡玩得開心！🥣")
