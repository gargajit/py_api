import requests
import json
import sys

if len(sys.argv) < 2:
    sys.exit()

response = requests.get("https://api.github.com/users/" + sys.argv[1])
obj = response.json()
print("Name:", obj["name"])
print("Public Repositories:", obj["public_repos"])
print("Follower Count:", obj["followers"])
print("Following Count:", obj["following"])
