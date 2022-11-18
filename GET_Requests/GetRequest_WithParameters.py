import requests

param= {'name':'Aslan', 'email':'aslanasaad@gmail.com', 'Number':'5517772123'}

response = requests.get("https://httpbin.org/get", params=param)
print(response.text)