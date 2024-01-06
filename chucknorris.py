import requests
import json

#Random ChuckNorris Jokes
'''
response = requests.get("https://api.chucknorris.io/jokes/random")
#print(json.dumps(response.json(), indent = 2))

obj = response.json()
print(obj["value"])
'''


# Get Categories
cat_response = requests.get("https://api.chucknorris.io/jokes/categories")

#Print the categries for user
categories = cat_response.json()
for category in categories:
    print(category, end=" ")

print()
#Prompt user to select the category
selected_category = input("Select a category: ")

#Print category related joke
if selected_category in categories:
    response = requests.get("https://api.chucknorris.io/jokes/random?category=" + selected_category)
    obj = response.json()
    print(obj["value"])
