import requests

url = "http://127.0.0.1:8000/users/"
req = requests.Session()
res = req.get(url=url)
print(res.json())
res_json = res.json()
assert res_json[0]['username'] == "admin"
