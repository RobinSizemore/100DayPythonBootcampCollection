from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url=wiki_url)
stats = driver.find_element(By.ID, "articlecount").find_element(By.TAG_NAME, "a")
print(stats.text)

search_toggle = driver.find_element(By.CLASS_NAME, value="search-toggle")
search_toggle.click()

search_bar = driver.find_element(By.NAME, value="search")
search_bar.send_keys("Robin")
search_bar.send_keys(Keys.RETURN)
