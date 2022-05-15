import sys
import json
from pymongo import MongoClient
from pprint import pprint
with open('env_mongo', 'r') as f:
    mongo_uri = f.readline()

client = MongoClient(mongo_uri)
db = client.website
args = sys.argv

coll = 'shop'
if args[2:]:
    coll = args[2]

key = 'doc'
if args[3:]:
    key = args[3]

value = 'index'
if args[4:]:
    value = args[4]

update_key = 'text'
update_val = 'This is.'

dat = {key: value,
       "title": "Welcome to",
       update_key: update_val
       }

json_dat = json.dumps(dat)
json_dat = json.loads(json_dat)


def main():
    getattr(sys.modules[__name__], args[1])()
    # rename_coll('ebay')
    pass

def find_one():
    res = db[coll].find_one({key: value}, {'_id': 0})
    pprint(res)


def find():
    res = list(db[coll].find({}, {'_id': 0}))
    pprint(res)


def insert():
    db[coll].insert_one(json_dat)


def list_coll():
    pprint(db.list_collection_names())


def remove_one():
    db[coll].delete_one({key: value})

def rename_coll():
    db[coll].rename(key)

def rename_field():
    db[coll].update_many({}, {"$rename": {"tool": "doc"}})

def update():
    query = {key: value}
    print(1, coll, 2, update_key, 3, update_val)
    values = {"$set": {update_key: update_val}}

    res = db[coll].update_one(query, values)

if __name__ == '__main__':
    main()
