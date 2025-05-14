# Ethical Price Tracker

Track prices from a public website (BooksToScrape), store historical prices, and build a dashboard to monitor trends and detect drops — all done ethically and programmatically.

✅ Problem Statement

How can we ethically track product prices over time to analyze pricing trends and notify users of drops — while respecting website usage policies and ensuring clean, scalable data handling?

## ✅ Step-by-Step Project Structure

## 📁 Folder Layout
ethical_price_tracker/
│
├── data/
│   ├── raw/                        # Raw scraped CSVs
│   └── book_prices.db              # SQLite database
│
├── scripts/
│   ├── __init__.py
│   ├── scrape.py                   # Ethical price scraper (Selenium + BeautifulSoup)
│   ├── store.py                    # CSV → SQLite storage logic
│   └── alert.py                    # (Optional) Price drop alert logic
│
├── dashboard/
│   └── app.py                      # Streamlit dashboard UI
│
├── requirements.txt
├── README.md
└── .gitignore
