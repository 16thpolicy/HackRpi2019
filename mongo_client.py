from pymongo import MongoClient
import datetime
import pprint

#client = MongoClient()
client = MongoClient('mongodb+srv://orllem:K0HASRQiKuv2vkMK@cluster0-ncjwb.gcp.mongodb.net/test?retryWrites=true&w=majority')

db = client.test_database

collection = db.test_collection


post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.list_collection_names())

pprint.pprint(posts.find_one())