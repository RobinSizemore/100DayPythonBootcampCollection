import dotenv
import requests
import os
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup  # I'd ordinarily just use selenium for this, but... assignment requirements.
import lxml
import time
import re
import selenium

dotenv.load_dotenv()
FAKE_ZILLOW = os.getenv("FAKE_ZILLOW")
FORM_URL = os.getenv("FORM_URL")

zillow_page = requests.get(url=FAKE_ZILLOW)
zillow_soup = BeautifulSoup(zillow_page.text, "lxml")
listings = zillow_soup.select("li.ListItem-c11n-8-84-3-StyledListCardWrapper")
to_write = []

for listing in listings:
    link = listing.select_one("a")['href']
    address = listing.select_one("address").text.strip()
    price = listing.select_one("div .PropertyCardWrapper span").text
    pattern = r"\$(\d{1,4}(?:,\d{3})*)(?:\+|\s*\/\s*mo)?"  # regex pattern to strip extra data
    fixed_price = re.search(pattern, price).group(1)
    print(fixed_price)
    to_write.append({"link": link,
                     "address": address,
                     "price": fixed_price})

# We have our listings, let's go to our google form.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=FORM_URL)

for writer in to_write:
    time.sleep(3)
    inputs = driver.find_elements(By.TAG_NAME, "input")
    submitter = driver.find_element(By.CSS_SELECTOR, "#mG61Hd div.RH5hzf.RLS9Fe div div.ThHDze div.DE3NNc.CekdCb "
                                                     "div.lRwqcd div span span")
    count = 0
    for this_input in inputs:
        if this_input.get_attribute("class") == "whsOnd zHQkBf":
            match count:
                case 0:
                    this_input.send_keys(writer["address"])
                case 1:
                    this_input.send_keys(writer["price"])
                case 2:
                    this_input.send_keys(writer["link"])
            count += 1
    submitter.click()
    time.sleep(1)
    returner = driver.find_element(By.LINK_TEXT, "Submit another response")
    returner.click()