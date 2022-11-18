import requests
import json
import jsonpath

def test_Add_new_data():
    API_URL="https://thetestingworldapi.com/api/studentsDetails"
    f = open("/Users/aslanasaad/Desktop/API/RequestJson.json", 'r')
    request_json = json.loads(f.read())
    response= requests.post(API_URL, request_json)
    id= jsonpath.jsonpath(response.json(), 'id')
    print(id[0])