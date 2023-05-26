import requests
import json

key = '506af92de4904752ae0b0ed6bb980099'
query = 'pasta'
maxFat = 25
url = 'https://spoonacular.com/food-api/docs#Search-Recipes-Complex?q={query}&max={maxFat}&app={key}'
payload = {'app': key}
response = requests.get(url, params=payload)
# print(response.status_code)
# print(response.headers['Content-Type'])
# print(response.text)
# print(type(response.text))
result_json = response.text
# print(type(result_json))
res = json.loads(result_json)
res_structured = json.dumps(res, indent=4)
print(res_structured)
r = result_json['results']
t = r['title']
print('title : ', t)
