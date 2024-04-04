import json
from openai import OpenAI
client = OpenAI()

prompt = "Give one activity suggestion for a day in Tokyo."

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content":  prompt},
  ]
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
  "prompt": prompt,
  "response_message": {
    "content": response_message.content,
    "role": response_message.role,
    },
  "model_used": model_used,
  })

with open(json_file_path, "w") as file:
  json.dump(historical_responses, file, indent=4)
  
print("Response stored in historical_responses.json")
