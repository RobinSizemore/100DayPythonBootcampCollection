import os
import requests

class NotificationManager:
    def __init__(self):
        self.telegram_bot_key = os.environ.get("TG_TOKEN")
        self.my_tg_id = "314128084"  # os.environ.get("TG_RECIPIENT")

    def send_message(self, message):
            telegram_req_params = {"chat_id": self.my_tg_id, "text": message}
            method = "sendMessage"
            telegram_url = f"https://api.telegram.org/bot{self.telegram_bot_key}/{method}"

            tg_response = requests.get(url=telegram_url, params=telegram_req_params)
            print(f"chatterbox: {tg_response.json()}")
            return tg_response
