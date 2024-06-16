import pprint


class FlightData:
    def __init__(self):
        pass

    def process_offers(self, offers):
        simplified = []
        for offer in offers:
            simple = {"price": offer["price"]["total"]}
            segments = offer["itineraries"][0]["segments"]
            simple["departure"] = segments[0]["departure"]["at"]
            simple["departure_iata"] = segments[0]["departure"]["iataCode"]
            simple["arrival"] = segments[len(segments) - 1]["arrival"]["at"]
            simple["arrival_iata"] = segments[len(segments) - 1]["arrival"]["iataCode"]
            simplified.append(simple)
        simplified.sort(key=lambda d: float(d["price"]))
        pprint.pprint(simplified)
