from urllib import request
import json
from pprint import pp
response = request.urlopen("https://jsonplaceholder.typicode.com/users")
json_response = response.read()
users = json.loads(json_response)
pp(users)
