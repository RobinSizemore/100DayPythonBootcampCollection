import os
import requests
import datetime as dt

nutritionix_app_id = os.environ.get("NUTRITIONIX_APP_ID")
nutritionix_api_key = os.environ.get("NUTRITIONIX_API_KEY")
nutritionix_url = "https://trackapi.nutritionix.com"
nutritionix_endpoint = nutritionix_url + "/v2/natural/exercise"

sheety_endpoint = os.environ.get("SHEETY_URL")
sheety_token = os.environ.get("SHEETY_TOKEN")
sheety_headers = {"Authorization": f"Bearer {sheety_token}"}

print(nutritionix_api_key)
print(nutritionix_app_id)

input_text = input("Tell me what kind of exercise(s) you did: ")

nutritionix_headers = {"x-app-id": nutritionix_app_id, "x-app-key": nutritionix_api_key}
nutritionix_params = {"query": input_text,
                      "weight_kg": 122.4,
                      "height_cm": 180,
                      "age": 45}
response = requests.post(url=nutritionix_endpoint,
                         json=nutritionix_params,
                         headers=nutritionix_headers)
if response.status_code != 200:
    print(response.text)
else:
    print(response.json())
exercises = response.json()["exercises"]

now = dt.datetime.now()
for exercise in exercises:
    new_workout = {"date": now.strftime("%d/%m/%Y"),
                   "time": now.strftime("%H:%M:%S"),
                   "exercise": exercise["name"],
                   "duration": exercise["duration_min"],
                   "calories": exercise["nf_calories"]}

    sheety_json = {"workout": new_workout}
    sheety_post_resp = requests.post(url=sheety_endpoint,
                                     headers=sheety_headers,
                                     json=sheety_json)

    if sheety_post_resp.status_code != 200:
        print("ERROR:" + sheety_post_resp.text)
    else:
        print(sheety_post_resp.json())

sheety_response = requests.get(url=sheety_endpoint,
                               headers=sheety_headers)
if sheety_response.status_code != 200:
    print("ERROR:" + sheety_response.text)
else:
    print(sheety_response.json())