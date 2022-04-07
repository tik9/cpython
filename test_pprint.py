from urllib import request
import json
from pprint import pp
response = request.urlopen("https://jsonplaceholder.typicode.com/users")
users = json.loads(response.read())
pp(users)
