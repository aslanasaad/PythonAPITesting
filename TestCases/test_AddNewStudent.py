import requests
import json
import jsonpath


def test_add_student_data():
    API_URL= "https://thetestingworldapi.com/api/studentsDetails"
    f= open("/Users/aslanasaad/Desktop/API/RequestJson.json", 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    print(response.text)


def test_update_student_data():
    API_URL= "https://thetestingworldapi.com/api/studentsDetails/3876842"
    f= open("/Users/aslanasaad/Desktop/API/RequestJson.json", 'r')
    json_request = json.loads(f.read())
    response = requests.post(API_URL, json_request)
    print(response.text)

def test_delete_student():
    API_URL= "https://thetestingworldapi.com/api/studentsDetails/3876842"
    response= requests.delete(API_URL)
    print(response.text)

def test_get_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/3876842"
    response= requests.get(API_URL)
    json_response = response.json()
    print(json_response)
    id= jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 3876842