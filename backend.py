import os
import json
from flask import Flask, render_template,jsonify
import numpy

#[ ] Set up server
#[ ] Get info from front end
#[ ] Save info into json
#[ ] host json file as location
#[ ] 
#[ ]

def parseGET(String):
    ret_val = String.split(',')
    return ret_val

#------------------------------------ flask code here
app = Flask(__name__)

# @app.route("/data")
# def returndata():
#     return render_template('data.json')
# @app.route("/",methods=['GET','POST'])
# def index():
#     if (request.method == 'POST'):
#         some_json = request.get_json()
#         return jsonify({'you sent': some_json}), 201
#     else:
#         return jsonify({"about":"Hello World!"})

@app.route('/<string:getrequest>',methods=['GET'])
def get_mulitply10(getrequest):
    args_ = parseGET(getrequest)


    return jsonify({'result':num})

if __name__ == '__main__':
    app.run(debug=True)
# ------------------------------------ 