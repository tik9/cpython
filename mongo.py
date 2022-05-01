import sys
import json
from pymongo import MongoClient
from pprint import pprint
with open('env_mongo', 'r') as f:
    mongo_uri = f.readline()

client = MongoClient(mongo_uri)
db = client.website
args = sys.argv

coll = 'pages'
if args[2:]:
    coll = args[2]

key = 'doc'
if args[3:]:
    key = args[3]
value = 'index'
if args[4:]:
    value = args[4]

update_key = 'text'
update_val = 'This is a website for programmers or for in programming interested people! Browse through the menu and look at the source in Github further down.'

dat = {key: value,
       "title": "Welcome to my site",
       update_key: update_val
       }

# print(type(dat))
json_dat = json.dumps(dat)
# print(type(json_dat))
json_dat = json.loads(json_dat)
# print(type(json_dat))


def main():
    # find_one()
    # find()
    # insert()
    # delete_one()
    function = getattr(sys.modules[__name__], args[1])
    function()
    pass


def update():
    query = {key: value}
    print(1, coll, 2, update_key, 3, update_val)
    values = {"$set": {update_key: update_val}}

    res = db[coll].update_one(query, values)


def find_one():
    res = db[coll].find_one({key: value}, {'_id': 0})
    pprint(res)


def find():
    res = list(db[coll].find({}, {'_id': 0}))
    pprint(res)


def insert():
    db[coll].insert_one(json_dat)


def delete_one():
    db[coll].delete_one({key: value})


if __name__ == '__main__':
    main()
