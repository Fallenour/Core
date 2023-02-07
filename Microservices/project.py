# from flask import Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")

def h():
  return "test"

in_memory_datastore = {
   "COBOL" : {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL" : {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL" : {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
}
@app.get('/programming_languages')
def list_programming_languages():
   return {"programming_languages":list(in_memory_datastore.values())}


# https://levelup.gitconnected.com/simple-api-using-flask-bc1b7486af88
@app.route("/message", methods=["GET"])
def message():
    posted_data = request.get_json()
    name = posted_data['name']
    return jsonify(" Hope you are having a good time " +  name + "!!!")

@app.route("/name", methods=["POST"])
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        return jsonify(str("Successfully stored  " + str(data)))

@app.route('/DRA', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


if __name__=="__main__":
  app.run(host="0.0.0.0", port=3790)

