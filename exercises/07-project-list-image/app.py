import requests

# your code herehttps
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

body1 = response.json()

project = body1[-1]

result = project["images"][-1]

print(result)







