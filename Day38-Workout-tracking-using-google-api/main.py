import requests
from datetime import datetime

APP_ID = "xxxxxxxxxx"
API_KEY = "xxxxxxxxx"
EXERCISE_ENDPOINT = "xxxxxxxx"
SHEETY_ENDPOINT = "xxxxxxxxx"
BEARER_ID = "xxxxxxxxx"

user_exercises = input("What exercises did you do today? ").lower()

user_params = {
    "query": user_exercises,
    "gender": "female",
    "weight_kg": 55,
    "height_cm": 159.6,
    "age": 20
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=EXERCISE_ENDPOINT, json=user_params, headers=headers)
#print(response.text)
data = response.json()
print(data)

today = datetime.now()
date_today = today.strftime("%d/%m/%Y")
time_now = today.strftime("%H:%M:%S")

for exercise in data["exercises"]:
    sheet_body = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_headers = {
    "Authorization": BEARER_ID
}

sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_body, headers=sheet_headers)
print(sheet_body)
