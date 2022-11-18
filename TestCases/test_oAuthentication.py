import json
import jsonpath
import requests

def test_oauth_api():
    API_URL="https://thetestingworldapi.com/api/StDetails/1104"
    response= requests.get(API_URL)
    print(response.text)