import dotenv
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

dotenv.load_dotenv()
LI_EMAIL = os.getenv("LI_EMAIL")
LI_PASS = os.getenv("LI_PASS")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.linkedin.com")

time.sleep(5)
print("Getting Fields")
username_input = driver.find_element(By.NAME, "session_key")
password_input = driver.find_element(By.ID, "session_password")
buttons = driver.find_elements(By.CLASS_NAME, value="btn-primary")
btn_found = False
for button in buttons:
    if button.get_attribute("data-tracking-control-name") == "homepage-basic_sign-in-submit-btn":
        sign_in_btn = button
        btn_found = True
        break
username_input.send_keys(LI_EMAIL)
password_input.send_keys(LI_PASS)
if btn_found:
    sign_in_btn.click()

# Login works - skipping the actual application part because I don't want to apply for a job.



