import requests

def get_titles():
    # your code here
    result=[]
    response = requests.get ("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    responseBody=response.json()
    for x in responseBody["posts"]:
        result.append(x["title"])
    return result
    
print(get_titles())

 