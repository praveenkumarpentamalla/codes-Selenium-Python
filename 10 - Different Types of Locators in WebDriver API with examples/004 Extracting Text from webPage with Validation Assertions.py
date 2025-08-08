from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Automatically downloads compatible driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://sso.teachable.com/secure/9521/identity/sign_up/otp")
driver.maximize_window()

print("Title:", driver.title)
print("URL:", driver.current_url)


driver.find_element(By.CSS_SELECTOR, "#name").send_keys("praveenkumar")
driver.find_element(By.CSS_SELECTOR, "#allowMarketingEmails").click()

driver.find_element(By.XPATH, "//button[@data-test='btn-signup']").click()

print("Output below")

print(driver.find_element(By.CLASS_NAME, "jdGIU").text)

print("Output above")

time.sleep(2)



driver.maximize_window()
driver.minimize_window()
