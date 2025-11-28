import streamlit as st
import os

# ===============================
#     PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Rossmann Sales Forecasting",
    layout="wide",
)


# ===============================
#     LOAD CSS
# ===============================
def load_css():
    css_path = "style.css"
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Файл style.css не знайдено!")


load_css()

# ===============================
#     SIDEBAR NAVIGATION
# ===============================

st.sidebar.title("📌 Навігація")
st.sidebar.markdown("Оберіть розділ:")

pages = {
    "📘 Огляд": "Overview",
    "📊 Дослідження даних (EDA)": "EDA",
    "🧱 Інженерія ознак": "Feature Engineering",
    "🤖 Порівняння моделей": "Models Comparison",
    "📈 Прогнози": "Predictions",
    "📉 Залишки (Residuals)": "Residuals",
    "🔥 SHAP Інтерпретація": "SHAP Explainability",
    "🏁 Висновки": "Conclusions",
}

# створюємо кнопки
for label, internal_name in pages.items():
    if st.sidebar.button(label):
        st.session_state["page"] = internal_name

# установка сторінки за замовчуванням
if "page" not in st.session_state:
    st.session_state["page"] = "Overview"

current_page = st.session_state["page"]

# ===============================
#     SWITCH PAGE LOGIC
# ===============================

# обчислюємо індекс файлу
page_index = list(pages.values()).index(current_page) + 1
file_name = f"{page_index}_{current_page.replace(' ', '_')}.py"

full_path = f"pages/{file_name}"

# перевіряємо, чи файл існує
if not os.path.exists(full_path):
    st.error(f"❌ Не знайдено файл сторінки: {full_path}")
else:
    st.switch_page(full_path)
