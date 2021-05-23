import requests
import base64
import couchdb
import sys
import config
import tweet_searcher, tweet_streaming
import threading
from TwitterAPI import TwitterAPI
import couchdb 

def streaming():
    #load variables from config
    keywords = config.keywords
    boxes = config.box_melb
    #boxes = config.melbourne_city

    # connect to db server
    couch = couchdb.Server(config.couchdb_url)

    # connect to database
    db = couch[config.couchdb_name]

    # create TwitterAPI object
    api = TwitterAPI(config.consumer_key,
                    config.consumer_secret,
                    config.access_token,
                    config.access_token_secret)
    tweet_streaming.filter_stream(api,db,keywords,boxes)
  
def search():

    # connect to db server
    couch = couchdb.Server(config.couchdb_url)

    # connect to database
    db = couch[config.couchdb_name]

    key_secret = '{}:{}'.format(config.consumer_key, config.consumer_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)

    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' }
    auth_data = {'grant_type': 'client_credentials'}
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    access_token = auth_resp.json()['access_token']
    search_headers = { 'Authorization': 'Bearer {}'.format(access_token) }

    tweet_searcher.search_tweets(config.search_query, config.states, config.states_geocodes, config.search_since, config.search_until, db, base_url, search_headers)


if __name__ == "__main__":
    t1 = threading.Thread(target=search, daemon=True)
    t2 = threading.Thread(target=streaming, daemon=True)
  
    # starting threads 
    t1.start()
    t2.start()

