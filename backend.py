import os
import json
from flask import Flask, render_template,jsonify,request
import numpy

#[ ] Set up server
#[ ] Get info from front end
#[ ] Save info into json
#[ ] host json file as location
#[ ] 
#[ ]

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
    #INSERT INTO DATABASE HERE
    return 201

@app.route('/allEvents/<string:getrequest>',methods=['GET'])
def GET_(getrequest):
    #args format example: ["allEvents", 4.5, [5.6,34.2]]
    args_ = parseGET(getrequest)

    #QUERY DATABASE HERE
    return jsonify({'result':args_})

if __name__ == '__main__':
    app.run(debug=True)
# ------------------------------------ 