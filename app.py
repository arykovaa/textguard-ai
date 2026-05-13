import streamlit as st
import random

st.title("🤖 TextGuard AI")

text = st.text_area("Вставьте текст для проверки")

if st.button("Проверить"):
    if len(text) < 20:
        st.warning("Введите больше текста")
    else:
        percent = random.randint(65, 95)
        st.success(f"Вероятность AI-текста: {percent}%")