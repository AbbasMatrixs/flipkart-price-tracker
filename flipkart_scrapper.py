from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Setup WebDriver
driver = webdriver.Chrome()

# List of Flipkart product URLs to track
products = [
    "https://www.flipkart.com/apple-iphone-14-pro-deep-purple-128-gb/p/itm75f73f63239fa",
    "https://www.flipkart.com/samsung-galaxy-s23-phantom-black-128-gb/p/itm89e2244ec0002",
]

data = []

for url in products:
    driver.get(url)
    time.sleep(3)  # Wait for page to load

    try:
        title = driver.find_element(By.CLASS_NAME, "B_NuCI").text.strip()
        price = driver.find_element(By.CLASS_NAME, "_30jeq3._16Jk6d").text
        print(f"🔍 {title} - {price}")
        
        data.append({"Product": title, "Price": price, "URL": url})
    except:
        print(f"⚠️ Could not retrieve data for {url}")

# Save data to CSV
df = pd.DataFrame(data)
df.to_csv("flipkart_prices.csv", index=False)

driver.quit()
print("✅ Data saved to flipkart_prices.csv")