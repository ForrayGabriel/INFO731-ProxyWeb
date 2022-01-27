import requests

resp = requests.get("http://127.0.0.1:8000/Ceciestuntest")
#resp = requests.get("http://forrayg.xyz/mass_shooting_us")

print(resp.text)
