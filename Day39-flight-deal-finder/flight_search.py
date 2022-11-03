import requests
from pprint import pprint
from flight_data import FlightData

FLIGHT_SEARCH_API = "xxxxxxxxx"
FLIGHT_SEARCH_ENDPOINT = "xxxxxxxxxx"


HEADERS = {
    "apikey": FLIGHT_SEARCH_API
}

parameters = {
    "term": "london",
    "location_types": "city"
    }

location_endpoint = f"{FLIGHT_SEARCH_ENDPOINT}/locations/query"


class FlightSearch:
    def __init__(self):
        self.city_codes = []
    def get_destination_code(self, city_names):
        print("get destination codes triggered")
        for city in city_names:
            parameters = {
                "term": city,
                "location_types": "city"
            }

            response = requests.get(url=location_endpoint, params=parameters, headers=HEADERS)
            results = response.json()
            #pprint(results)
            code = results["locations"][0]["code"]
            #print(f"RESULTS: {results}")
            self.city_codes.append(code)
        return self.city_codes.append(code)

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(
            url=f"{FLIGHT_SEARCH_ENDPOINT}/v2/search",
            headers=HEADERS,
            params=query,
        )

        try:
            data = response.json()["data"][0]
            print(f"{destination_city_code} {data['price']}")
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data