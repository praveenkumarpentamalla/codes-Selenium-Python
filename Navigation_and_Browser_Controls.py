from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatically downloads compatible driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://aarouundme.com/")
driver.maximize_window()

print("Title:", driver.title)
print("URL:", driver.current_url)

driver.get("https://management.divsolution.com/")

driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
