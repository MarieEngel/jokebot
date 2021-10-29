import requests

query = "https://v2.jokeapi.dev/joke/Any?lang=de&blacklistFlags=nsfw,religious,racist,sexist,explicit"

response = requests.get(query).json()

print(response)

joke = []
if response['type'] == "twopart":
    joke.append(response['setup'])
    joke.append(response['delivery'])
if response['type'] == 'single':
    joke.append(response['joke'])

print(joke)
