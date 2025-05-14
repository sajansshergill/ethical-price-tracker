import pandas as pd
import sqlite3
import os

def store_data(csv_path="data/raw/book_prices.csv", db_path="data/book_prices.db"):
    if not os.path.exists(csv_path):
        print("❌ CSV not found. Run scraper first.")
        return

    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql("prices", conn, if_exists="append", index=False)
    conn.close()
    print(f"✅ Stored {len(df)} records in {db_path}")

if __name__ == "__main__":
    store_data()
    