import json
from unicodedata import name
from pymongo import MongoClient
from pprint import pprint
with open('env_mongo', 'r') as f:
    mongo_uri = f.readline()

client = MongoClient(mongo_uri)
db = client.website
coll = 'pages'
doc = 'code'
field = 'doc'

json_dat = '''
{"doc": "",
"title":"",
"text":""
}
'''

json_dat = json.loads(json_dat)


def main():
    # pprint(json_dat)
    find_one()
    # find()
    # insert()
    pass


def find_one():
    # res = getattr(db, coll)
    res = db[coll].find_one({field: doc}, {'_id': 0})
    pprint(res)


def find():
    res = getattr(db, coll)
    res = list(db[coll].find({}, {'_id': 0}))
    pprint(res)


def insert():
    db[coll].insert_one(json_dat)


if __name__ == '__main__':
    main()
