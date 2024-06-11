import requests
from datetime import datetime
import pytz
import time


def iss_checker():
    # Charleston WV Lat Long
    CWV_LAT = 38.349819
    CWV_LNG = -81.632622

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    parameters = {
        "lat": CWV_LAT,
        "lng": CWV_LNG,
        "formatted": 0,
    }

    iss_near = False
    if abs(CWV_LAT - iss_latitude) <= 5 and abs(CWV_LNG - iss_longitude) <= 5:
        iss_near = True

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Parse the sunrise and sunset times into datetime objects
    sunrise_str = data["results"]["sunrise"]
    sunset_str = data["results"]["sunset"]

    # The times are in UTC and in ISO 8601 format, so you can parse them like this:
    sunrise = datetime.fromisoformat(sunrise_str).replace(tzinfo=pytz.UTC)
    sunset = datetime.fromisoformat(sunset_str).replace(tzinfo=pytz.UTC)

    # Convert the times to your local timezone
    your_tz = pytz.timezone("America/New_York")  # Replace with your actual timezone
    sunrise = sunrise.astimezone(your_tz)
    sunset = sunset.astimezone(your_tz)

    # Get the current time
    time_now = datetime.now(your_tz)

    # Check if it's dark
    is_dark = not (sunrise <= time_now < sunset)

    # If the ISS is close to my current position,
    # and it is currently dark
    if is_dark and iss_near:
        # I'm not sending an email, because I don't want to put the credentials in this code.
        print("HEY! LOOK UP!")
    else:
        print("Carry on.")
    # Then email me to tell me to look up.
    # BONUS: run the code every 60 seconds.
    time.sleep(120)
    iss_checker()


iss_checker()
