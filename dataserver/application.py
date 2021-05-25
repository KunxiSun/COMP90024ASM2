from flask import Flask, jsonify, abort, request, make_response, url_for

import sys 
sys.path.append("Service") 
import couchdbService

app = Flask(__name__, static_url_path = "")

# Error Handling
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

# API
'''
### Name: test
### API: '/test/count'
### Description: ''
'''
@app.route('/sa_employ_allcity_allyear', methods = ['GET'])
def sa_employ_allcity_allyear():
    data = couchdbService.sa_employ_allcity_allyear()
    result = {"data":data,"isSuccess":True}
    return jsonify( result ), 200

@app.route('/employ_allcity', methods = ['GET'])
def employ_allcity():
    data = couchdbService.employ_allcity()
    result = {"data":data,"isSuccess":True}
    return jsonify( result ), 200

@app.route('/wordfrequency_allcity_allyear', methods = ['GET'])
def wordfrequency_allcity_allyear():
    data = couchdbService.wordfrequency_allcity_allyear()
    result = {"data":data,"isSuccess":True}
    return jsonify( result ), 200

if __name__ == '__main__':
    #couchdbService.jobRelatedTweetsDistribution()
    app.run(port=5000,debug=True,threaded=True,host='0.0.0.0')

