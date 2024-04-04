import json
from openai import OpenAI
client = OpenAI()

prompt = "Give one activity suggestion for a day in Tokyo."

messages = [
    {"role": "user", "content": "Advice on a trip with the given information"},
    {"role": "user", "content": "Start Destination: Tokyo"},
    {"role": "user", "content": "End Destination: Kyoto"},
    {"role": "user", "content": "Duration: 4 weeks"},
    {"role": "user", "content": "Budget: $7000"},
    {"role": "user", "content": "Points of Interest: Mount Fuji, Kyoto"},
    {"role": "user", "content": "Interests: Hiking, Fishing, Food, Sleeping in a ryokan"}
]

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=messages
)

response_message = completion.choices[0].message
model_used = completion.model

print(response_message)

json_file_path = "historical_responses.json"

try:
  with open(json_file_path, "r") as file: 
    historical_responses = json.load(file)
except FileNotFoundError:
  print("file not found!")
  historical_responses = []

historical_responses["responses"].append({
  "prompt": messages,
  "response_message": {
    "content": response_message.content,
    "role": response_message.role,
    },
  "model_used": model_used,
  })

with open(json_file_path, "w") as file:
  json.dump(historical_responses, file, indent=4)
  
print("Response stored in historical_responses.json")



"""
Trip information collection: 

To help plan your trip, I'll need some information from you. Please provide the following details:

1. Start Destination: Where will your trip begin?
2. End Destination: Where will your trip end?
3. Duration: How many days will your trip last?
4. Budget: What is your estimated budget for the trip?
5. Points of Interest: What specific places or attractions would you like to visit during your trip? (e.g., cities, mountains, lakes, landmarks, shops)
6. Interests: What activities or experiences are you interested in? (e.g., fishing, hiking, shopping, cultural experiences)

Feel free to provide as much detail as possible to help tailor your trip suggestion to your preferences.
"""