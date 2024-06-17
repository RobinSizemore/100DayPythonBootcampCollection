from bs4 import BeautifulSoup
import dotenv
import os
import requests
import lxml
from pprint import pprint
import notification_manager

dotenv.load_dotenv()
AMAZON_URL = os.getenv("AMAZON_URL")
headers = {"User-Agent": os.getenv("HDR_AGENT"),
           "Accept-Language": os.getenv("HDR_ACCEPT_LANGUAGE")}
response = requests.get(url=AMAZON_URL, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
dollars = soup.find_all(name="span", class_="a-price-whole")[0].text.split("<")[0]
cents = soup.find_all(name="span", class_="a-price-fraction")[0].text
price = float(f"{dollars}{cents}")

with open("price") as file:
    old_price = float(file.readline())

if old_price > price:
    # Send a message.
    chatterbot = notification_manager.NotificationManager()
    chatterbot.send_message(f"Price on your Soundcore Headphones is {price}")
    # Write new price to file.
    with open("price", "w") as file:
        file.write(f"{price}")
