#Random Cat facts 
import requests
import json

response = requests.get("https://catfact.ninja/fact?max_length=140")
obj = response.json()
print(obj["fact"])
