#This file will need to use the DataManager,
# FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
import notification_manager
import data_manager
import flight_search
import flight_data

# Lookup Cities
dm = data_manager.DataManager()
cities = dm.get_cities()

flight_data = flight_data.FlightData()
chatterbox = notification_manager.NotificationManager()
better_offer_found = False

for city in cities:
    # Lookup Flights
    flights = flight_search.FlightSearch()
    offers = flights.flight_offer_search("CRW", city["iataCode"])
    offer_price = offers[0]["price"]["total"]
    print(offer_price)
    # If best price so far:
    if float(offer_price) < city["lowestPrice"]:
        print(f"{city["city"]} - {offer_price}")
        better_offer_found = True
        # Send notification
        chatterbox = notification_manager.NotificationManager()
        chatterbox.send_message(f"Lowest price yet for {city["city"]}. "
                                f"{offer_price}")
        city["lowestPrice"] = offer_price

if better_offer_found:
    dm.update_cities(cities)
