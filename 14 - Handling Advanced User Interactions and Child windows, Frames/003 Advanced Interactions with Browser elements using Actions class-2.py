from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)


menu = driver.find_element(By.ID, "mousehover")
action.move_to_element(menu).perform()
childmenu = driver.find_element(By.LINK_TEXT, "Reload")

action.move_to_element(childmenu).click().perform()


