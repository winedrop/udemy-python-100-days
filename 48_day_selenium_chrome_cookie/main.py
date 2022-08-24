from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(5)

browser.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = browser.find_element(By.ID,"cookie")


t_end = time.time() + 10
while time.time() < t_end:
    cookie.click()

print(browser.find_element(By.ID,"money").text)
browser.quit()