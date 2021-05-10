import requests

res = requests.get('http://api.open-notify.org/iss-now.json')
print(res.json())
print(res.json()['iss_position']['latitude'])
