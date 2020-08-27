import requests
import json
url = 'https://yesno.wtf/api'
a = requests.get(url)
v = json.loads(a.text)
b = input("n or y:")
if b == "y":
    c = "answer"
else:
    c = "forced"
print(v[c])