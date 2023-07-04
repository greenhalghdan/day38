import requests
from datetime import datetime as dt
import os
# https://developer.nutritionix.com/admin/access_details
# natural language query
app_id = os.environ["app_id"]
app_key = os.environ["app_key"]
url_nutritionx = os.environ["url_nutritionx"]
sheety_token = os.environ["sheety_token"]
sheet_url = os.environ["sheet_url"]

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key,
    "Content-Type": "application/json"

}
exercise_input = input("What exercise have you done? \n")

exercise = {
    "query": exercise_input
}

response = requests.post(url=url_nutritionx, json=exercise, headers=headers)
exercise = response.json()

# adding row to sheet
headers_sheety = {
    "Authorization": sheety_token
}

for ex in exercise["exercises"]:
    current_time = dt.now()
    sheet_params = {
          "workout": {
              "date": current_time.strftime('%d/%m/%Y'),
              "time": current_time.strftime('%H:%M'),
              "exercise": ex["name"],
              "duration": ex["duration_min"],
              "calories": ex["nf_calories"]
          }
        }
    sheety_response = requests.post(url=sheet_url, json=sheet_params, headers=headers_sheety)

    print(sheety_response.json())