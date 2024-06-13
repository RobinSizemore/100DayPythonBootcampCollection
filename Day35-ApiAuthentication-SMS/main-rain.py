import requests
import datetime as dt
import os

telegram_bot_key = os.environ.get("TG_TOKEN")
openweather_api_key = os.environ.get("OWM_API_KEY")
my_tg_id = os.environ.get("TG_RECIPIENT")
my_latitude = os.environ.get("MY_LAT")
my_longitude = os.environ.get("MY_LNG")


# Get the weather for the next few days.
req_params = {"appid": openweather_api_key,
              "lat": my_latitude,
              "lon": my_longitude}

req_url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=req_url, params=req_params)


# Determine when it will rain next.
rain_expected = False
looped = 0
rain_expected_in = 0
for prediction in response.json()["list"]:
    looped += 1
    when = dt.datetime.fromtimestamp(prediction["dt"])
    now = dt.datetime.now()
    is_going_to_rain = prediction["weather"][0]["main"] == "Rain"
    if is_going_to_rain:
        rain_expected = True
        difference = when - now
        rain_expected_in = round(difference.total_seconds() / 3600)
        break  # We already know.  So stop.

if rain_expected:
    msg_text = f"Rain is expected in about {rain_expected_in} hours."
else:
    msg_text = "Rain is not expected in the next few days."

telegram_req_params = {"chat_id": my_tg_id, "text": msg_text}
method = "sendMessage"
telegram_url = f"https://api.telegram.org/bot{telegram_bot_key}/{method}"

tg_response = requests.get(url=telegram_url, params=telegram_req_params)

