from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def get_price(url):
    options = Options()

    # 🔥 anti-bot tricks
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)
    time.sleep(5)

    try:
        price_element = driver.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen")
        price_text = price_element.get_attribute("innerHTML")

        # clean ₹ and commas
        price = price_text.replace("₹", "").replace(",", "").strip()

        driver.quit()
        return int(float(price))

    except Exception as e:
        print("Error:", e)
        driver.quit()
        return None