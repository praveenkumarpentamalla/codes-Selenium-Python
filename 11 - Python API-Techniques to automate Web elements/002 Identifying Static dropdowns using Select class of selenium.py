
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Automatically downloads compatible driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("praveen")
driver.find_element(By.NAME, "email").send_keys("praveen@example.com")
driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("kumar")
driver.find_element(By.ID, "exampleCheck1").click()

time.sleep(2)

## DROP DOWN 

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value("M")

time.sleep(2)

driver.find_element(By.XPATH, "//input[@value='Submit']").click()

print(driver.find_element(By.CLASS_NAME, "alert-success").text )


print("Title:", driver.title)
print("URL:", driver.current_url)

time.sleep(2)

