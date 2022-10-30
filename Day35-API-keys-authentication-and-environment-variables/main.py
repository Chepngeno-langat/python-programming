import requests

api_key1 = "8c66c322c1e50bd8a059d13f2e3b3b8c"
api_key2 = "826ce9bf20babc2664761fb5707b3450"

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
