import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit()

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + sys.argv[1] +"&APPID=fd58feb6ef13b1c10bdcf80f97071d64")
#print(response.json())

obj = response.json()
#print(obj)
#print(obj["coord"]["lon"])

print("longitude", obj["coord"]["lon"])
print("latitude", obj["coord"]["lat"])

