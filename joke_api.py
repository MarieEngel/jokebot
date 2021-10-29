import requests


def get_joke(language):
    return extract_joke(call_joke_api(language))


def call_joke_api(language):
    query = f'https://v2.jokeapi.dev/joke/Any?lang={language}&blacklistFlags=nsfw,religious,racist,sexist,explicit'
    return requests.get(query).json()


def extract_joke(response):
    result = []
    if response['type'] == 'twopart':
        result.append(response['setup'])
        result.append(response['delivery'])
    if response['type'] == 'single':
        result.append(response['joke'])
    return result
