from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
# options.add_argument("start-maximized")

chrome_profile_path = "/home/sad1/git/freebet/profile"
options.add_argument(f"user-data-dir={chrome_profile_path}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        )


driver.get("https://betboom.ru/actions#online")


def promo(code):
    driver.find_element(By.ID, 'promocode').send_keys(code)
    time.sleep(random.randint(2, 8)/10)
    driver.find_element(By.ID, "buttonpromo").click()
    time.sleep(random.randint(2, 8)/10)
