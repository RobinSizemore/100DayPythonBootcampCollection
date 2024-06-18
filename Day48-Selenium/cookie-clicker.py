import selenium.common.exceptions
from selenium import webdriver
import datetime as dt
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wiki_url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url=wiki_url)

cookie = driver.find_element(By.ID, value="cookie")

start = dt.datetime.now()
print(start)

store = driver.find_element(By.ID, value="store")
store_items = store.find_elements(By.CSS_SELECTOR, value="#store div")
store_ids = [store_item.get_attribute("id") for store_item in store_items]
store_ids.reverse()

def buy_from_store(store_ids):
    for store_id in store_ids:
        item = driver.find_element(By.ID, store_id)
        is_not_grey = False
        try:
            is_not_grey = item.get_attribute("class").find("grayed") == -1
        except selenium.common.exceptions.StaleElementReferenceException:
            is_not_grey = False
        if is_not_grey:
            try:
                item.click()
            except selenium.common.exceptions.StaleElementReferenceException:
                print("Item went stale.")


five_secs_out = start + dt.timedelta(seconds=5)
print(f"{five_secs_out}")

while start + dt.timedelta(minutes=5) > dt.datetime.now():
    cookie.click()
    if dt.datetime.now() > five_secs_out:
        buy_from_store(store_ids)
        five_secs_out = dt.datetime.now() + dt.timedelta(seconds=5)
        print(f"{five_secs_out}")

cps = driver.find_element(By.ID, "cps").text
print(f"Final {cps}")
