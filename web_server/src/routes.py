from flask import *
import couchdb

app = Flask(__name__)
app.secret_key = """U29tZWJvZHkgb25jZSB0b2xkIG1lIFRoZSB3b3JsZCBpcyBnb25uYSBy
b2xsIG1lIEkgYWluJ3QgdGhlIHNoYXJwZXN0IHRvb2wgaW4gdGhlIHNoZWQgU2hlIHdhcyBsb29r
aW5nIGtpbmRhIGR1bWIgV2l0aCBoZXIgZmluZ2VyIGFuZCBoZXIgdGh1bWIK"""

couchdb_url = "http://admin:admin@172.26.130.11:5984"
couchdb_table_name = 'whole_au'

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message' : 'Hello world!'})

@app.route('/search', methods=['POST','GET'])
def search_tweet():
    couch = couchdb.Server(couchdb_url)
    db = couch[couchdb_table_name]

    mango = {
        "selector": {},
        "limit": 20,
        "skip": 0
    }
    docs = db.find(mango)
    res= []
    for doc in docs:
        print(doc)
        res.append(doc)

    return jsonify({"count":len(res), "docs":res})

@app.route('/search/<doc_id>', methods=['POST','GET'])
def search_tweet_by_id(doc_id):
    couch = couchdb.Server(couchdb_url)
    db = couch[couchdb_table_name]
    print(doc_id)
    doc = db[doc_id]
    return doc

@app.route('/delete/<doc_id>', methods=['POST','GET'])
def delete_tweet_by_id(doc_id):
    
    couch = couchdb.Server(couchdb_url)
    db = couch[couchdb_table_name]
    doc = db[doc_id]
    db.delete(doc)
    return jsonify({"ok":True,"id":doc_id})    
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'