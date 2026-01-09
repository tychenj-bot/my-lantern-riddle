import streamlit as st
import random
import time

# 設定網頁標題
st.set_page_config(page_title="元宵闖關大賽", page_icon="🏮")

# 1. 題庫設計 (分為三個等級)
if 'game_data' not in st.session_state:
    st.session_state.levels = {
        1: {
            "name": "🏮 第一關：初試啼聲 (入門)",
            "questions": [
                {"q": "一個老頭子，頭上長鬍子，脫下綠袍子，滿身金珠子。（猜一植物）", "a": "玉米", "hint": "黃色的，一粒一粒"},
                {"q": "身穿綠衣裳，肚裡紅瓤子，生的兒子多，個個黑臉子。（猜一水果）", "a": "西瓜", "hint": "夏天消暑聖品"},
                {"q": "紅紅小臉似蘋果，雖然掉進水火裡，最後卻變白胖子。（猜一應景食物）", "a": "元宵", "hint": "圓圓的，甜甜的"},
                {"q": "長長耳朵紅眼睛，走路愛跳不愛跑。（猜一動物）", "a": "兔子", "hint": "愛吃胡蘿蔔"}
            ]
        },
        2: {
            "name": "🔥 第二關：漸入佳境 (進階)",
            "questions": [
                {"q": "左邊綠，右邊紅，左右相遇起涼風。（猜一字）", "a": "秋", "hint": "禾+火"},
                {"q": "一隻八寶袋，樣樣都能裝。能聽又能說，說話響噹噹。（猜一電子產品）", "a": "手機", "hint": "現代人離不開它"},
                {"q": "沒嘴會說話，沒腳會走路，天天提醒我，早起去讀書。（猜一生活用品）", "a": "鬧鐘", "hint": "會叮嚀你起床"},
                {"q": "一人走進去，兩人撐著它，天晴沒它事，下雨才帶它。（猜一物品）", "a": "傘", "hint": "擋雨用的"}
            ]
        },
        3: {
            "name": "🏆 第三關：登峰造極 (大師)",
            "questions": [
                {"q": "兩點水。（猜一字）", "a": "冰", "hint": "水結凍了"},
                {"q": "一口吃掉牛尾巴。（猜一字）", "a": "告", "hint": "上面是牛，下面是口"},
                {"q": "七十二小時。（猜一字）", "a": "晶", "hint": "三個日"},
                {"q": "守門員。（猜一字）", "a": "閃", "hint": "門裡面有人"}
            ]
        }
    }
    # 初始化遊戲狀態
    st.session_state.current_level = 1
    st.session_state.correct_in_level = 0
    st.session_state.total_score = 0
    st.session_state.game_finished = False
    # 隨機選題
    for i in [1, 2, 3]:
        random.shuffle(st.session_state.levels[i]["questions"])

# 介面顯示
st.title("🏮 元宵燈謎闖關大挑戰")

if not st.session_state.game_finished:
    lv = st.session_state.current_level
    current_lv_data = st.session_state.levels[lv]
    
    st.header(current_lv_data["name"])
    st.write(f"目前等級進度：已答對 **{st.session_state.correct_in_level} / 3** 題")
    st.progress(st.session_state.correct_in_level / 3)

    # 取得當前題目 (根據已答對的數量當索引)
    q_idx = st.session_state.correct_in_level
    current_q = current_lv_data["questions"][q_idx]

    with st.container(border=True):
        st.subheader(f"題目：{current_q['q']}")
        user_ans = st.text_input("輸入答案：", key=f"q_{lv}_{q_idx}").strip()
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("提交答案"):
                if user_ans == current_q['a']:
                    st.session_state.correct_in_level += 1
                    st.session_state.total_score += 1
                    
                    # 檢查是否過關
                    if st.session_state.correct_in_level >= 3:
                        if lv < 3:
                            # 晉級特效
                            st.success(f"🎊 恭喜通過 {current_lv_data['name']}！")
                            if lv == 1:
                                st.balloons() # 第一關特效：氣球
                            elif lv == 2:
                                st.balloons()
                                st.toast("🚀 太強了！下一關難度提升！") # 第二關多一個提示
                            
                            time.sleep(1)
                            st.session_state.current_level += 1
                            st.session_state.correct_in_level = 0
                        else:
                            st.session_state.game_finished = True
                        st.rerun()
                    else:
                        st.success("✅ 答對了！繼續下一題！")
                        time.sleep(1)
                        st.rerun()
                else:
                    st.error("❌ 不太對喔，再想一下！")
        
        with col2:
            if st.button("💡 拿提示"):
                st.info(f"提示：{current_q['hint']}")

else:
    # 終極過關特效 (最精彩)
    st.balloons()
    st.snow()
    st.markdown("# 🏆 恭喜成為【燈謎大宗師】！")
    st.write(f"你成功通過了所有關卡，總共答對了 {st.session_state.total_score} 題。")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJqZ3R4bm56Z3R4bm56Z3R4bm56Z3R4bm56Z3R4bm56Z3R4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l0MYt5jPR6QX5pnqM/giphy.gif")
    
    if st.button("重新挑戰"):
        st.session_state.current_level = 1
        st.session_state.correct_in_level = 0
        st.session_state.total_score = 0
        st.session_state.game_finished = False
        st.rerun()

# 側邊欄
with st.sidebar:
    st.write("### 🎮 遊戲規則")
    st.write("1. 共有三個關卡：入門、進階、大師。")
    st.write("2. 每個關卡需答對 **3 題** 即可晉級。")
    st.write("3. 難度會隨著關卡提升，特效也會越來越華麗！")
    st.divider()
    st.write("祝明天 1/10 打高爾夫球順利！⛳")
