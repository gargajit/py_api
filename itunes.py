import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

'''
#let's write a python code using requests that pretend to be web browser requsting API
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
json = response.json()
print(json["resultCount"])
'''

'''
#let's improve the view of json by importing json package and using dumps function
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent = 2))
'''

#let's increase the limit to 10 and let's take the only thing we wish for i.e. trackName
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
obj = response.json()
for result in obj["results"]:
    print(result["trackName"])
