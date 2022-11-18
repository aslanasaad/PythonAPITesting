import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

# Read input json file
file = open('//Users//aslanasaad//Desktop//API//CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

#print(request_json)

# Make post request with json input body

response= requests.post(url, request_json)

# Validating response code
assert response.status_code == 201

# Fetch Header from Response
print(response.headers.get('Content-Length'))

# Parse response to json Format
response_json = json.loads(response.text)

# Pick ID using json Path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])
