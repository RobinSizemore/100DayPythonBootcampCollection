# -- ISS Scratch --
# import json
# import requests
# import datetime as dt
#
# print(f"Start at {dt.datetime.now()}")
# iss = requests.get(url="http://api.open-notify.org/iss-now.json")
# if iss.status_code == 200:
#     print(iss.json())
# else:
#     iss.raise_for_status()
# print(f"END at {dt.datetime.now()}")

# -- Sunrise-Sunset --
import requests
import datetime as dt
import pytz


# Charleston WV Lat Long
CWV_LAT = 38.349819
CWV_LNG = -81.632622

params = {"lat": CWV_LAT, "lng": CWV_LNG}

response = requests.get(url="https://api.sunrise-sunset.org/json",
                        params=params)
sunrise_utc_str = response.json()["results"]["sunrise"]
sunset_utc_str = response.json()["results"]["sunset"]

# Parse the time strings into datetime objects
sunrise_utc = dt.datetime.strptime(sunrise_utc_str, "%I:%M:%S %p")
sunset_utc = dt.datetime.strptime(sunset_utc_str, "%I:%M:%S %p")

# Make the datetime objects timezone-aware
utc_tz = pytz.timezone("UTC")
sunrise_utc = utc_tz.localize(sunrise_utc)
sunset_utc = utc_tz.localize(sunset_utc)

# Convert the times to your local timezone
your_tz = pytz.timezone("America/New_York")  # Replace with your actual timezone
sunrise_local = sunrise_utc.astimezone(your_tz)
sunset_local = sunset_utc.astimezone(your_tz)

if response.status_code == 200:
    print(f"Sunrise is {sunrise_local.strftime("%I:%M:%S %p")}")
    print(f"Sunset is {sunset_local.strftime("%I:%M:%S %p")}")
    print(f"It is now {dt.datetime.now().strftime("%I:%M:%S %p")}")
else:
    response.raise_for_status()
