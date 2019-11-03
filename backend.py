import os
import json
from flask import Flask, render_template,jsonify,request
import numpy
from pymongo import MongoClient
import pprint

#[ ] Set up server
#[ ] Get info from front end
#[ ] Save info into json
#[ ] host json file as location
#[ ] 
#[ ]

client = MongoClient('mongodb+srv://orllem:K0HASRQiKuv2vkMK@cluster0-ncjwb.gcp.mongodb.net/test?retryWrites=true&w=majority')
db = client.test_database
collection = db.test_collection
posts = db.posts

#parses incoming get request
def parseGET(String):
    parsing = String.split(',')
    parsing[0] = float(parsing[0])
    parsing_temp = parsing[1].replace('[','').replace(']','').split(':')
    parsing_temp[0]=float(parsing_temp[0])
    parsing_temp[1]=float(parsing_temp[1])
    return [parsing[0],parsing_temp]

def parsePOST(String):
    json_acceptable_string = String.replace("'", "\"")
    ret_val = json.loads(json_acceptable_string)
    return ret_val

#------------------------------------ flask code here
app = Flask(__name__)

@app.route("/newEvent",methods=['POST'])
def POST_():
    json_post = request.get_json()
    #inserts post into database
    post_id = posts.insert_one(json_post).inserted_id
    return 201

@app.route('/allEvents/<string:getrequest>',methods=['GET'])
def GET_(getrequest):
    #args format example: [4.5, [5.6,34.2]]
    radius,center = parseGET(getrequest)
    center = np.asarray(center)

    neighborhood = list()
    for post in posts.find():
        neighborhood.append(post['location'])

    neighborhood = np.asarray(neighborhood)

    center = points[np.random.randint(0,50)]
    radius = 10
    indices = np.where(np.linalg.norm(points-center,axis=1)<=radius)
    irrelevant_indices = np.delete(np.arange(50),indices)
    irrelevant_points = points[irrelevant_indices]
    # print("indicies",indices)
    relevantpoints = points[indices]
    #mean center
    #normalize

    #QUERY DATABASE HERE
    return jsonify({'result':relevantpoints})

if __name__ == '__main__':
    app.run(debug=True)
# ------------------------------------ 