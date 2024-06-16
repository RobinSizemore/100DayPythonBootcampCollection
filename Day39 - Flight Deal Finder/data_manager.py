import requests
import os
import pprint


class DataManager:
    def __init__(self):
        self.resp = None
        self.sheety_endpoint = os.environ.get("SHEETY_URL")
        self.sheety_token = os.environ.get("SHEETY_TOKEN")
        self.sheety_headers = {"Authorization": f"Bearer {self.sheety_token}"}
        self.cities = []
        print(self.sheety_headers)

    def get_cities(self):
        self.resp = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        if self.resp.status_code != 200:
            print(self.resp.text)
        else:
            for city in self.resp.json()["prices"]:
                new_city = {"city": city["city"], "iataCode": city["iataCode"],
                            "lowestPrice": city["lowestPrice"], "id": city["id"]}
                self.cities.append(new_city)
        return self.cities

    def update_cities(self, updated_cities):
        for city in updated_cities:
            updated = {"price": {"city": city["city"],
                                 "iataCode": city["iataCode"],
                                 "lowestPrice": city["lowestPrice"]}}
            self.resp = requests.put(url=f"{self.sheety_endpoint}/{city["id"]}",
                                     headers=self.sheety_headers,
                                     json=updated)
            print("Sheety")
            print(self.resp.json())
