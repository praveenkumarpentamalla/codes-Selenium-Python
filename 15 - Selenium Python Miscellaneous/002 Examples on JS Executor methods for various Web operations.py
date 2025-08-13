from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "name").send_keys("hello")
print(driver.find_element(By.NAME, "name").text)

print(driver.find_element(By.NAME, "name").get_attribute("value"))

shopButton = driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")

driver.execute_script("arguments[0].click();",shopButton)
time.sleep(3)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)
