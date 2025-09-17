import streamlit as st
import gspread
from datetime import datetime, timedelta
from google.oauth2.service_account import Credentials
import pandas as pd

# --- Google Sheet 认证 ---
SHEET_NAME = "Habits"

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
CREDS_FILE = "credentials.json"

@st.cache_resource
def connect_sheet():
    creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1  # 默认第一张表
    return sheet

sheet = connect_sheet()

# --- Streamlit 页面设置 ---
st.set_page_config(page_title="习惯评分记录器", layout="centered")
st.title("📝 每日习惯评分")

# --- 输入表单 ---
habit_options = ["读书", "锻炼", "写作", "早睡", "冥想"]
habit = st.selectbox("选择习惯", habit_options)
score = st.slider("你昨天在这个习惯上的努力程度？", 0, 10)
yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")

submit = st.button("提交评分")

if submit:
    try:
        sheet.append_row([yesterday, habit, score])
        st.success(f"✅ 已记录：{yesterday} - {habit} - {score}分")
    except Exception as e:
        st.error(f"⚠️ 提交失败：{e}")

# --- 展示历史记录 ---
st.divider()
st.subheader("📊 评分历史")

try:
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    if not df.empty:
        df = df.sort_values(by="date", ascending=False)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("暂无评分记录")
except Exception as e:
    st.error(f"⚠️ 无法读取数据：{e}")
