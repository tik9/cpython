import sys
import json
from pymongo import MongoClient
from pprint import pprint
with open('.env', 'r') as f:
    mongo_uri = f.readline().split('=')[1]

client = MongoClient(mongo_uri)
db = client.website
args = sys.argv

coll = 'sys'
# coll = 'test'
# if args[2:]:
# coll = args[2]

key = 'name'
val = ''
update_key = ''
update_val = ''

dat = {key: val, '': '', update_key: update_val}

json_dat = json.dumps(dat)
json_dat = json.loads(json_dat)


def main():
    key = None
    if args[2:]:
        key = args[2]
    value = None
    if args[3:]:
        value = args[3]

    getattr(sys.modules[__name__], args[1])(key, value)
    # rename_field('cat','category')
    pass


def find_one(key, value):
    print(coll, key, value)
    res = db[coll].find_one({key: value}, {'_id': 0})
    pprint(res)


def find(*args):
    res = list(db[coll].find({}, {'_id': 0}))
    pprint(res)


def insert(*args):
    db[coll].insert_one(json_dat)


def list_coll(*args):
    pprint(db.list_collection_names())


def remove_one(key, val):
    db[coll].delete_one({key: val})


def rename_coll(key):
    db[coll].rename(key)


def rename_field(old, new):
    db[coll].update_many({}, {"$rename": {old: new}})


def update(*args):
    query = {key: val}
    values = {"$set": {update_key: update_val}}

    db[coll].update_one(query, values)


if __name__ == '__main__':
    main()
