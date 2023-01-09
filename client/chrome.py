from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import socket
import random
import time
import logging

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--window-size=1920,1080")
options.add_argument("--remote-debugging-port=9222")

# options.add_argument("start-maximized")

port = int(open("socket.txt").readline())
options.add_argument(f"user-data-dir=/home/USERNAME/bb-freebet/profile")
# options.add_argument(f"user-data-dir=/home/2happy/git/bb-freebet/client/profile")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options, service=ChromeService(
    ChromeDriverManager().install()))
# driver = webdriver.Chrome(options=options, service=Service(
#     executable_path=chrome_driver_path))

logging.basicConfig(
    # (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        # logging.StreamHandler()  # Вывод в консоль
        logging.FileHandler(f'log.txt'),
    ]
)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        )


driver.get("https://betboom.ru/actions#online")

logging.warning("start!")


def promo(code):
    driver.find_element(By.ID, 'promocode').send_keys(code)
    time.sleep(random.randint(2, 5)/10)
    driver.find_element(By.ID, "buttonpromo").click()


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("localhost", port))
logging.warning(f"bind to {port}")

data = b''

while True:
    buffer, addr = sock.recvfrom(1024)
    data += buffer
    logging.warning(f"accept data: {buffer.decode("utf-8")}")
    if b'<END>' in data:
        messages = data.split(b'<END>')
        for i in messages[:-1]:
            logging.warning(f"using promo {i.decode()}")
            promo(i.decode("utf-8"))
        data = messages[-1]
