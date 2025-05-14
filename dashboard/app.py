import streamlit as st
import pandas as pd
import sqlite3
import os

# Page setup
st.set_page_config(page_title="📉 Book Price Tracker", layout="wide")
st.title("📚 Ethical Price Tracker Dashboard")

# Load data from SQLite database
@st.cache_data
def load_data():
    db_path = "data/book_prices.db"
    if not os.path.exists(db_path):
        return pd.DataFrame()
    
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM prices", conn)
    conn.close()
    
    # Ensure timestamp is parsed as datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

df = load_data()

# Main UI
if not df.empty:
    st.success(f"✅ Loaded {len(df)} price records.")

    with st.expander("📋 Full Price History"):
        st.dataframe(df)

    selected_book = st.selectbox("📖 Choose a Book", sorted(df["title"].unique()))

    book_df = df[df["title"] == selected_book].sort_values("timestamp")

    st.subheader(f"💰 Price History for: {selected_book}")
    if len(book_df) > 1:
        st.line_chart(book_df.set_index("timestamp")["price"])
    else:
        st.info("Not enough data to show a trend. Please run the scraper multiple times.")
else:
    st.warning("⚠️ No data found. Please run `scripts/scrape.py` and `scripts/store.py` first.")
