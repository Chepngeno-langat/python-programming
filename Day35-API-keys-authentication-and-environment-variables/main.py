import requests

api_key1 = "12345"
api_key2 = "12345"

parameter1 = {
    "q": "Nairobi,Kenya",
    "appid": api_key1,
}

parameter2 = {
    "lat": -1.2833,
    "lon": 36.8167,
    # "exclude": {
    #     "current",
    #     "minutely",
    #     "daily",
    #     "alerts",
    # },
    "appid": api_key1,
}

response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=parameter1)
data = response.json()
#print(data)

hourly_response = requests.get("http://api.openweathermap.org/data/2.5/onecall", params=parameter2)
hourly_data = hourly_response.json()
print(hourly_response.status_code)
print(hourly_data)
