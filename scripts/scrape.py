import os
import time
import random
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin

def scrape_prices():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Base URL used for both scraping and link joining
    base_url = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
    driver.get(base_url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    books = []
    for product in soup.select("article.product_pod"):
        try:
            title = product.h3.a["title"]
            raw_price = product.select_one(".price_color").text.replace("£", "").strip()
            price = float(raw_price)

            # Simulate more visible price variation for testing
            price += random.uniform(-5.0, 5.0)

            availability = product.select_one(".availability").text.strip()
            relative_link = product.h3.a["href"]
            url = urljoin(base_url, relative_link)

            books.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "title": title,
                "price": round(price, 2),
                "availability": availability,
                "url": url
            })
        except Exception as e:
            print(f"⚠️ Skipping a product due to error: {e}")
            continue

    df = pd.DataFrame(books)

    # Save to CSV
    os.makedirs("data/raw", exist_ok=True)
    csv_path = "data/raw/book_prices.csv"

    if os.path.exists(csv_path):
        df.to_csv(csv_path, mode="a", header=False, index=False)
    else:
        df.to_csv(csv_path, index=False)

    print(f"✅ Scraped {len(df)} products → saved to {csv_path}")

if __name__ == "__main__":
    scrape_prices()
    