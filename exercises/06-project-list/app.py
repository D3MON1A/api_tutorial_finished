import requests

response1 = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")

variable2= response1.json()

print(variable2[1] ["name"])