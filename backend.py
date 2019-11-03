import os
import json
from flask import Flask, render_template,jsonify,request
import numpy as np
from pymongo import MongoClient
import pprint

#[ ] Set up server
#[ ] Get info from front end
#[ ] Save info into json
#[ ] host json file as location
#[ ] 
#[ ]



#parses incoming get request
def parseGET(String):
    #radius=8.0&x=10.2&y=11.3
    parsing = String.split('&')
    #radius=8.0, x=10.2, y=11.3
    parsing[0] = float(parsing[0].split('=')[1])
    #parsing = [8.0, x=10.2, y=11.3]
    parsing[1] = float(parsing[1].split('=')[1])
    #parsing = [8.0, 10.2, y=11.3]
    parsing[2] = float(parsing[2].split('=')[1])

    return [parsing[0],parsing[1],parsing[2]]

def parsePOST(String):
    json_acceptable_string = String.replace("'", "\"")
    ret_val = json.loads(json_acceptable_string)
    return ret_val

#------------------------------------ flask code here
app = Flask(__name__)

@app.route("/",methods=['POST'])
def index():
    # print("Posts:",posts)
    if(request.method == 'POST'):
        json_post = request.get_json()
        #inserts post into database
        posts.insert_one(json_post)
        return {"message":"ok"},201
    return {"message":"not ok"},500

@app.route('/allEvents',methods=['GET'])
def GET_():
    radius = float(request.args.get("radius"))
    x = float(request.args.get("x"))
    y = float(request.args.get("y"))
    #args format example: [4.5, [5.6,34.2]]
    # radius,x,y = parseGET(getrequest)
    center = np.asarray([x,y])

    neighborhood = list()
    for post in posts.find():
        x,y =post['location'][0]
        x=float(x)
        y=float(y)
        # print([x,y])
        neighborhood.append([x,y])

    neighborhood = np.asarray(neighborhood)
    # print(neighborhood)
    indices = np.where(np.linalg.norm(neighborhood-center,axis=1)<=radius)
    irrelevant_indices = np.delete(np.arange(neighborhood.shape[0]),indices)
    irrelevant_points = neighborhood[irrelevant_indices]
    # print("indicies",indices)
    relevantpoints = neighborhood[indices]
    dictionary = dict()
    for i in range(relevantpoints.shape[0]):
        dictionary["point"+str(i)] = relevantpoints[i].tolist()
    print(dictionary)

    return dictionary,201

if __name__ == '__main__':

    client = MongoClient('mongodb+srv://orllem:K0HASRQiKuv2vkMK@cluster0-ncjwb.gcp.mongodb.net/test?retryWrites=true&w=majority')
    db = client.test_database
    collection = db.test_collection
    posts = db.posts
    print("Posts:",posts)
    app.run(debug=True)
# ------------------------------------ 