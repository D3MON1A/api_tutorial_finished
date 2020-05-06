import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")
if response.status_code == 404:
    print ("The URL you asked is not found")
elif response.status_code == 503:
    print ("Unavailable right now")
elif response.status_code == 200:
    print("Everythign went perfect")
elif response.status_code == 400:
    print ("Something is wrong on the request params")
else: 
    print ("Something else" +str (response.status_code))