import requests

query = "https://v2.jokeapi.dev/joke/Any?lang=de&blacklistFlags=nsfw,religious,racist,sexist,explicit"

response = requests.get(query)
payload = response.json()

print(payload)
