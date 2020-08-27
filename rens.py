import requests
import json

url = 'https://pokeapi.co/api/v2/pokemon/pikachu/'

a = requests.get(url)
v = json.loads(a.text)
print(v)