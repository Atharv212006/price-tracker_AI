from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_price(url):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")

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

        price = price_text.replace("₹", "").replace(",", "").strip()

        driver.quit()
        return int(float(price))

    except:
        driver.quit()
        return None