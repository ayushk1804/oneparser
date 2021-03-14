import os

# TODO fix mod prem 
# os.system("wget https://t.mytbot.workers.dev/0:/pandoc")

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.errorhandler(404)
def not_found(e):
    return jsonify("This is not the correct page")


@app.route("/api/pandoc", methods=["GET", "POST"])
def pandoc():
    if request.method == "POST":    
        text = str(request.json['inputData'])
        with open('stext','w') as sft:
            sft.write(text)
        
        cmd = './'+str(request.json['cmd'])
        os.system(cmd)
        with open('otext', 'r') as oft:
            contents = oft.read()
        return jsonify(contents)
        # print(request.json)
        # return "HPOST"

    if request.method == "GET":
        return "The api is working as expected"

app.run()