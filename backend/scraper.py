from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 🔥 PRICE FUNCTION (Amazon)
def get_price(url):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
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

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".a-price .a-offscreen"))
        )

        price_element = driver.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen")
        price_text = price_element.get_attribute("innerHTML")

    time.sleep(5)

    try:
        price_element = driver.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen")
        price_text = price_element.get_attribute("innerHTML")

        # clean ₹ and commas
        price = price_text.replace("₹", "").replace(",", "").strip()

        driver.quit()
        return int(float(price))

    except:
        driver.quit()
        return None


# 🔥 SIZE FUNCTION (AJIO)
def check_size_available(url, target_size):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".size-variant-item"))
        )

        sizes = driver.find_elements(By.CSS_SELECTOR, ".size-variant-item")

        for size in sizes:
            text = size.text.strip().upper()

            if text == target_size.upper():
                classes = size.get_attribute("class")

                if "instock" in classes.lower():
                    driver.quit()
                    return True
                else:
                    driver.quit()
                    return False

        driver.quit()
        return None

    except:
    except Exception as e:
        print("Error:", e)
        driver.quit()
        return None