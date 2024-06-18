from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org")
events_div = driver.find_element(By.CLASS_NAME, "event-widget")
line_items = events_div.find_elements(By.TAG_NAME, "li")
dict = {}
index = -1
for line_item in line_items:
    index += 1
    time = line_item.find_element(By.TAG_NAME, "time")
    event = {"time": time.get_attribute("datetime")}
    anchor = line_item.find_element(By.TAG_NAME, "a")
    event["description"] = anchor.text
    event["link"] = anchor.get_attribute("href")
    dict[index] = event
pprint(dict)
driver.quit()
