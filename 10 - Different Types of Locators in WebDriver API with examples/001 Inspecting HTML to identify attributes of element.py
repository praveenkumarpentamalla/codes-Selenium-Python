from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

# Automatically download and setup the ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get("https://management.divsolution.com/")
driver.maximize_window()

# Print title and URL
print("Title:", driver.title)
print("URL:", driver.current_url)

# Locate the email input using the correct name or ID
# From your HTML: name="email_temp", id="id_email"
driver.find_element(By.NAME, "email_temp").send_keys("praveenkumar")

# Alternatively, using ID:
# driver.find_element(By.ID, "id_email").send_keys("praveenkumar")
