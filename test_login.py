from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os

# Path to chromedriver
chromedriver_path = r"C:\Users\CHARUARJUN\Documents\Selenium_tests\chromedriver.exe"
service = Service(chromedriver_path)

# Start Chrome
driver = webdriver.Chrome(service=service)

# Open the local login page
login_html_path = r"C:\Users\CHARUARJUN\Documents\Selenium_tests\FoodApp\login.html"
driver.get(f"file:///{login_html_path}")

sleep(1)

# Fill username and password
driver.find_element(By.ID, "username").send_keys("user1")
driver.find_element(By.ID, "password").send_keys("1234")

# Click login button
driver.find_element(By.ID, "loginBtn").click()

#sleep(2)  # wait to see result
input("Press Enter to close the browser...")
driver.quit()