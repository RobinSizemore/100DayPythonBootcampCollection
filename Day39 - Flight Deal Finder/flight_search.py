import os
import requests
import pprint
import datetime as dt
import amadeus


class FlightSearch:
    def __init__(self):
        self.amadeus = None
        self.depart_date = None
        self.api_key = os.environ.get("AMADEUS_KEY")
        self.api_secret = os.environ.get("AMADEUS_SECRET")
        self.amadeus_endpoint = "https://test.api.amadeus.com"

    def flight_offer_search(self, depart_city, arrive_city):
        self.amadeus = amadeus.Client(client_id=self.api_key,
                                      client_secret=self.api_secret)
        self.depart_date = (dt.datetime.now() + dt.timedelta(days=3)).strftime("%Y-%m-%d")

        response = self.amadeus.shopping.flight_offers_search.get(originLocationCode=depart_city,
                                                                  destinationLocationCode=arrive_city,
                                                                  departureDate=self.depart_date,
                                                                  adults=1)
        data = response.data
        data.sort(key=lambda d: float(d["price"]["total"]))
        return data
