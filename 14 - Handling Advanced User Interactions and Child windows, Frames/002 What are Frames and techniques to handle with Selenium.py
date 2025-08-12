from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/iframe")

wait = WebDriverWait(driver, 10)

# Wait for popup and close if it appears
try:
    close_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.tox-notification__dismiss")))
    close_btn.click()
except:
    print("No popup appeared")

# Now switch to iframe
driver.switch_to.frame("mce_0_ifr")

# Use JavaScript to bypass read-only mode if needed
driver.execute_script('document.getElementById("tinymce").contentEditable = true;')

# Clear & set text
body = driver.find_element(By.ID, "tinymce")
body.clear()
body.send_keys("I am able to automate this now!")

driver.switch_to.default_content()

print(driver.find_element(By.TAG_NAME, "h3").text)

