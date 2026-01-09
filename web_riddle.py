import streamlit as st
import random
import time

# 設定網頁標題
st.set_page_config(page_title="元宵燈謎大混戰", page_icon="🏮")

# --- 1. 混合題庫 (謎語 + 腦筋急轉彎 + 諧音哏) ---
if 'game_initialized' not in st.session_state:
    raw_levels = {
        1: {
            "name": "🐣 第一關：歡樂新手村",
            "pool": [
                {"q": "什麼雞沒有翅膀？ (腦筋急轉彎)", "a": "田雞", "options": ["田雞", "肉雞", "弱雞", "肯德基"], "hint": "它其實是一種青蛙"},
                {"q": "什麼布剪不斷？ (傳統謎語)", "a": "瀑布", "options": ["帆布", "瀑布", "桌布", "膠布"], "hint": "在大自然的山中"},
                {"q": "什麼水不能喝？ (腦筋急轉彎)", "a": "薪水", "options": ["汽水", "薪水", "淚水", "墨水"], "hint": "爸爸媽媽每個月最想看到的"},
                {"q": "麒麟到了北極會變成什麼？ (諧音哏)", "a": "冰淇淋", "options": ["北極麟", "冰淇淋", "死麒麟", "白麒麟"], "hint": "冰 + 麒麟 = ?"},
                {"q": "為什麼電腦會感冒？ (諧音哏)", "a": "因為它有Windows", "options": ["因為過熱", "因為有Windows", "因為病毒", "因為沒關機"], "hint": "Windows 的諧音像什麼？(聞到死/聞到涕)"},
                {"q": "什麼鍵盤沒有字？ (傳統謎語)", "a": "琴鍵", "options": ["手機鍵盤", "電腦鍵盤", "琴鍵", "收銀機"], "hint": "跟音樂有關"},
                {"q": "哪種水果最容易跌倒？ (諧音哏)", "a": "狐狸", "options": ["企鵝", "狐狸", "兔子", "香蕉"], "hint": "腳滑 = 狡猾 (題目是陷阱，雖然問水果但答案是動物)"},
                {"q": "什麼路不能走？ (腦筋急轉彎)", "a": "網路", "options": ["馬路", "鐵路", "網路", "絲路"], "hint": "你現在就在這條路上"},
                {"q": "年紀並不大，鬍子一把抓，不論遇到誰，總愛喊媽媽。(傳統謎語-猜動物)", "a": "羊", "options": ["羊", "貓", "狗", "猴子"], "hint": "咩～咩～"},
                {"q": "什麼人最不聽話？ (腦筋急轉彎)", "a": "聾子", "options": ["壞人", "小孩", "聾子", "學生"], "hint": "因為他「聽不到」"}
            ]
        },
        2: {
            "name": "🤔 第二關：腦力進階戰",
            "pool": [
                {"q": "哪種動物最愛管閒事？ (諧音哏)", "a": "海鮮", "options": ["小狗", "管家婆", "海鮮", "大象"], "hint": "因為「管很寬」(管海產)"},
                {"q": "米的爸爸是誰？ (諧音哏)", "a": "花", "options": ["稻子", "農夫", "花", "泥土"], "hint": "因為：花生米"},
                {"q": "一頭公牛加一頭母牛。 (猜三個字-腦筋急轉彎)", "a": "兩頭牛", "options": ["生小牛", "兩頭牛", "配成對", "一對牛"], "hint": "不要想太複雜"},
                {"q": "左邊綠，右邊紅，左右相遇起涼風。(傳統謎語-猜一字)", "a": "秋", "options": ["秋", "和", "利", "種"], "hint": "禾 + 火"},
                {"q": "哪種病最不花錢？ (腦筋急轉彎)", "a": "窮病", "options": ["感冒", "窮病", "相思病", "沒病"], "hint": "因為沒錢治"},
                {"q": "什麼東西越洗越髒？ (傳統謎語)", "a": "水", "options": ["衣服", "水", "毛巾", "肥皂"], "hint": "洗完東西後，它變色了"},
                {"q": "為什麼企鵝只有肚子是白的？ (諧音/腦筋急轉彎)", "a": "手短洗不到背", "options": ["天生的", "防敵色", "手短洗不到背", "為了美觀"], "hint": "這是一個非常「冷」的理由"},
                {"q": "一隻八寶袋，樣樣都能裝。能聽又能說，說話響噹噹。(傳統謎語-猜電子產品)", "a": "手機", "options": ["電視", "收音機", "手機", "電腦"], "hint": "現代人最愛"},
                {"q": "什麼老鼠愛亂買東西？ (諧音哏)", "a": "斑馬", "options": ["錢鼠", "斑馬", "袋鼠", "米老鼠"], "hint": "身上全是「條碼」"},
                {"q": "哪種球不能打？ (腦筋急轉彎)", "a": "地球", "options": ["網球", "地球", "棒球", "皮球"], "hint": "我們住的地方"}
            ]
        },
        3: {
            "name": "🧠 第三關：大師終極戰",
            "pool": [
                {"q": "星星、月亮、太陽，誰是啞巴？ (諧音哏)", "a": "星星", "options": ["星星", "月亮", "太陽", "都是"], "hint": "星星知我心 (知音人不在)"},
                {"q": "七十二小時。(傳統謎語-猜一字)", "a": "晶", "options": ["晶", "明", "三", "旬"], "hint": "三個日"},
                {"q": "哪種水果會預言？ (諧音哏)", "a": "香蕉", "options": ["蘋果", "香蕉", "奇異果", "木瓜"], "hint": "蕉好運 (交好運)"},
                {"q": "守門員。(傳統謎語-猜一字)", "a": "閃", "options": ["閂", "閉", "閃", "問"], "hint": "門裡面有人"},
                {"q": "巧克力和口香糖打架，巧克力贏了。(諧音哏-猜一食物)", "a": "巧克力塊", "options": ["巧克力塊", "口香糖片", "夾心酥", "士力架"], "hint": "巧克力「快」(塊)"},
                {"q": "一家有四口，還要養隻狗。(傳統謎語-猜一字)", "a": "器", "options": ["囂", "哭", "器", "突"], "hint": "四個口 + 犬"},
                {"q": "什麼東西放在火上燒不爛，放進水裡卻會爛？ (腦筋急轉彎)", "a": "紙", "options": ["鐵", "紙", "石頭", "塑膠"], "hint": "書本的材質"},
                {"q": "哪種職業的人最希望你跌倒？ (腦筋急轉彎)", "a": "物理治療師", "options": ["醫生", "路人", "推拿師", "物理治療師"], "hint": "跌倒才需要復健"},
                {"q": "兩點水。(傳統謎語-猜一字)", "a": "冰", "options": ["冰", "冷", "冬", "凍"], "hint": "水結冰了"},
                {"q": "什麼鍵盤沒有字？ (重覆檢查-換題) 哪種動物最愛管閒事？ (重複-換題) 米的外公是誰？ (諧音哏)", "a": "爆", "options": ["稻", "爆", "土", "風"], "hint": "爆米花"}
            ]
        }
    }

    st.session_state.levels = {}
    for i in [1, 2, 3]:
        shuffled_pool = random.sample(raw_levels[i]["pool"], 10)
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
st.title("🏮 元宵燈謎主題大混戰")

if not st.session_state.game_finished:
    lv = st.session_state.current_level
    current_lv_data = st.session_state.levels[lv]
    
    st.subheader(f"當前進度：{current_lv_data['name']}")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write(f"本關答對：**{st.session_state.correct_in_level} / 3**")
    with col_b:
        st.write(f"剩餘題目：**{10 - st.session_state.q_pool_idx}**")
    
    st.progress(st.session_state.correct_in_level / 3)

    if st.session_state.q_pool_idx < 10:
        current_q = current_lv_data["questions"][st.session_state.q_pool_idx]

        with st.container(border=True):
            st.markdown(f"### Q{st.session_state.q_pool_idx + 1}: {current_q['q']}")
            
            cols = st.columns(2)
            for i, option in enumerate(current_q["options"]):
                with cols[i % 2]:
                    if st.button(option, key=f"btn_{lv}_{st.session_state.q_pool_idx}_{i}", use_container_width=True):
                        if option == current_q["a"]:
                            st.success("✅ 答對了！太聰明了！")
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
                                st.toast(f"🚀 通關！準備進入第 {st.session_state.current_level} 關")
                            else:
                                st.session_state.game_finished = True
                        st.rerun()
            
            if st.button("💡 拿小提示 (不跳題)"):
                st.info(f"提示：{current_q['hint']}")
    else:
        st.error("😭 本關題目用完了，答對數不足 3 題...")
        if st.button("重考本關 (題目會重新洗牌)"):
            st.session_state.correct_in_level = 0
            st.session_state.q_pool_idx = 0
            random.shuffle(st.session_state.levels[lv]["questions"])
            st.rerun()

else:
    # --- 3. 通關畫面 (啦啦隊版) ---
    st.balloons()
    st.snow()
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🏆 恭喜成為【全能謎題大師】！</h1>", unsafe_allow_html=True)
    st.write(f"在三關的大混戰中，你總共拿下了 {st.session_state.total_score} 分！")
    
    # 更新這裡：換成啦啦隊的 GIF
    st.image("https://media.giphy.com/media/l41lYCDgxP665gjVm/giphy.gif", caption="啦啦隊為你的智慧喝采！🎉")
    
    if st.button("再玩一次，題目會重新隨機抽取"):
        del st.session_state['game_initialized']
        st.rerun()

# --- 4. 側邊欄 (移除高爾夫球內容) ---
with st.sidebar:
    st.write("### 🏮 元宵節快樂！")
    st.write("祝大家：")
    st.write("1. 身體健康，萬事如意 🍊")
    st.write("2. 湯圓吃甜甜，好運連連 🥣")
    st.write("3. 猜燈謎得大獎 🎁")
    st.divider()
    st.write("**遊戲規則：**")
    st.write("* 每關隨機 10 題，混合三種題型。")
    st.write("* 只要答錯就會直接跳下一題！")
    st.write("* 必須累積答對 3 題才能晉級。")
