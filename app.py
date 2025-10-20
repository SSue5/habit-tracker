import streamlit as st
import sqlite3
from datetime import datetime, timedelta
import pandas as pd

# --- SQLite 数据库设置 ---
DB_FILE = "habit_tracker.db"

def init_db():
    """初始化数据库，创建表结构"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            habit TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_record(date, habit, score):
    """插入一条记录"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO habits (date, habit, score) VALUES (?, ?, ?)", (date, habit, score))
    conn.commit()
    conn.close()

def fetch_records():
    """获取所有记录"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT date, habit, score FROM habits ORDER BY date DESC")
    records = cursor.fetchall()
    conn.close()
    return records

# 初始化数据库
init_db()

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
        insert_record(yesterday, habit, score)
        st.success(f"✅ 已记录：{yesterday} - {habit} - {score}分")
    except Exception as e:
        st.error(f"⚠️ 提交失败：{e}")

# --- 展示历史记录 ---
st.divider()
st.subheader("📊 评分历史")

try:
    records = fetch_records()
    if records:
        df = pd.DataFrame(records, columns=["日期", "习惯", "评分"])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("暂无评分记录")
except Exception as e:
    st.error(f"⚠️ 无法读取数据：{e}")
