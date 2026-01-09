import streamlit as st
import random

# 設定網頁標題與圖示
st.set_page_config(page_title="元宵猜燈謎大賽", page_icon="🏮")

# 初始化遊戲資料 (存放在 session_state 中，確保網頁重整時資料不會消失)
if 'riddles' not in st.session_state:
    st.session_state.riddles = [
        {"q": "一個老頭子，頭上長鬍子，脫下綠袍子，滿身金珠子。（猜一植物）", "a": "玉米", "hint": "這是一種常見的五穀雜糧，黃色的"},
        {"q": "身穿綠衣裳，肚裡紅瓤子，生的兒子多，個個黑臉子。（猜一水果）", "a": "西瓜", "hint": "夏天最受歡迎，甜美多汁"},
        {"q": "紅紅小臉似蘋果，雖然掉進水火裡，最後卻變白胖子。（猜一應景食物）", "a": "元宵", "hint": "這不就是我們今天的主角嗎？"},
        {"q": "左邊綠，右邊紅，左右相遇起涼風。（猜一字）", "a": "秋", "hint": "禾苗是綠的，火是紅的"},
        {"q": "一隻八寶袋，樣樣都能裝。能聽又能說，說話響噹噹。（猜一電子產品）", "a": "手機", "hint": "你現在可能正用著它"}
    ]
    random.shuffle(st.session_state.riddles)
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.game_over = False

# 網頁視覺標題
st.title("🏮 元宵節猜燈謎大賽")
st.write(f"目前得分：**{st.session_state.score}**")

# 檢查遊戲是否結束
if st.session_state.current_index < len(st.session_state.riddles):
    current_q = st.session_state.riddles[st.session_state.current_index]
    
    # 顯示題目卡片
    st.info(f"### 第 {st.session_state.current_index + 1} 題\n{current_q['q']}")
    
    # 使用者輸入
    user_answer = st.text_input("請輸入你的答案：", key=f"input_{st.session_state.current_index}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("送出答案"):
            if user_answer == current_q['a']:
                st.success("🎉 太棒了！答對了！")
                st.session_state.score += 1
                # 稍微延遲後進入下一題 (在實際應用中，通常會讓使用者點擊「下一題」)
            else:
                st.error(f"❌ 不太對喔，答案是「{current_q['a']}」")
            
            # 不論對錯，都準備進入下一題
            st.session_state.current_index += 1
            st.button("下一題 →")
            
    with col2:
        if st.button("💡 獲取提示"):
            st.warning(f"提示：{current_q['hint']}")

else:
    # 結算畫面
    st.balloons()
    st.success("🎊 恭喜完成所有題目！")
    st.metric("最終總分", f"{st.session_state.score} 點")
    
    if st.button("重新開始遊戲"):
        st.session_state.current_index = 0
        st.session_state.score = 0
        random.shuffle(st.session_state.riddles)
        st.rerun()

# 側邊欄說明
with st.sidebar:
    st.header("遊戲說明")
    st.write("1. 閱讀題目後在輸入框填寫答案。")
    st.write("2. 點擊「送出答案」判定結果。")
    st.write("3. 真的想不出來可以點擊「獲取提示」。")
    st.divider()
    st.write("祝大家元宵節快樂！🍵")
  
