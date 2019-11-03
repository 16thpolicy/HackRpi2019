from pymongo import MongoClient
import datetime
import pprint
import numpy as np

#client = MongoClient()
client = MongoClient('mongodb+srv://orllem:K0HASRQiKuv2vkMK@cluster0-ncjwb.gcp.mongodb.net/test?retryWrites=true&w=majority')

db = client.test_database

collection = db.test_collection


#post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}

descriptions = ["people are dying", "We have a pregnant woman", "We are alive","We are trapped","We are in problem"]
urgencys = ["green","yellow","red"]

description = np.random.choice(descriptions)
urgency = np.random.choice(urgencys)
radius = np.random.uniform(low=5, high=10, size=1)
people = int(np.random.randint(low=5, high=10, size=1))
location = np.random.uniform(low=0.5, high=43.3, size=(1,2)).tolist()

print("location", location)


post = {"location": location,
         "people": people,
         "urgency": urgency,
         "description": description}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.list_collection_names())

# pprint.pprint(posts.find_one())

for post in posts.find():
    pprint.pprint(post)

# pprint.pprint(posts)