import requests
import os
import datetime as dt

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")

# CREATE USER
# pixela_params = {"token": PIXELA_TOKEN,
#                  "username": PIXELA_USERNAME,
#                  "agreeTermsOfService": "yes",
#                  "notMinor": "yes"}
#
# response = requests.post(url="https://pixe.la/v1/users", json=pixela_params)
# print(response.text)

# CREATE GRAPH
# graph_endpoint = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs"
# graph_params = {
#                 "id": "biking",
#                 "name": "Time on Bike",
#                 "color": "shibafu",  # Green
#                 "type": "int",
#                 "unit": "minutes",
#                 "tz": "America/New_York"
#                 }
# pixela_header = {
#                 "X-USER-TOKEN": PIXELA_TOKEN
#                 }
# response = requests.post(url=graph_endpoint, json=graph_params, headers=pixela_header)
# print(response.text)

# ADD PIXEL
# today = dt.datetime.now()
# today_str = today.strftime('%Y%m%d')
# biking_endpoint = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/biking"
# biking_params = {
#                 "date": today_str,
#                 "quantity": "15"
#                 }
# pixela_header = {
#                 "X-USER-TOKEN": PIXELA_TOKEN
#                 }
# response = requests.post(url=biking_endpoint, json=biking_params, headers=pixela_header)
# print(response.text)

# UPDATE PIXEL
# today = dt.datetime.now()
# today_str = today.strftime('%Y%m%d')
# biking_endpoint = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/biking/{today_str}"
# biking_params = {
#                 "quantity": "25"
#                 }
# pixela_header = {
#                 "X-USER-TOKEN": PIXELA_TOKEN
#                 }
# response = requests.put(url=biking_endpoint, json=biking_params, headers=pixela_header)
# print(response.text)

# DELETE PIXEL
today = dt.datetime.now()
today_str = today.strftime('%Y%m%d')
biking_endpoint = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/biking/{today_str}"
pixela_header = {
                "X-USER-TOKEN": PIXELA_TOKEN
                }
response = requests.delete(url=biking_endpoint, headers=pixela_header)
print(response.text)
