import requests

# your code here

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")

print("Content-Type is ", response.headers['Content-Type'])
print(response.text)
variable1 = response.json() 



print(variable1["name"] )