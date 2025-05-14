# Ethical Price Tracker

Track prices from a public website (BooksToScrape), store historical prices, and build a dashboard to monitor trends and detect drops — all done ethically and programmatically.

✅ Problem Statement
How can we ethically track product prices over time to analyze pricing trends and notify users of drops — while respecting website usage policies and ensuring clean, scalable data handling?

## ✅ Step-by-Step Project Structure

## 📁 Folder Layout
ethical_price_tracker/
│
├── data/
│   └── raw/                        # Stores scraped price history CSV
│
├── scripts/
│   ├── scrape_prices.py           # Scraper using Selenium + BeautifulSoup
│   ├── store_prices.py            # Store prices into SQLite
│   └── price_alerts.py            # (Optional) Alert on price drop
│
├── streamlit_app.py               # Streamlit dashboard to visualize prices
├── requirements.txt
├── .gitignore
└── README.md


