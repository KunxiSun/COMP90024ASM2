from os import stat_result
from TwitterAPI import TwitterAPI
import TwitterStream
import couchdb 
import config

#load variables from json
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret
keywords = config.keywords
#boxes = config.melbourne_city
boxes = config.box_melb
url = config.db_url
##dbname = config.db_name
#connect to db server
##couch = couchdb.Server(url)
#connect to database
##db = couch[dbname]
#create TwitterAPI object
api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token,
                 access_token_secret)
<<<<<<< HEAD:harvester/twitterHarvester.py
TwitterStream.filter_stream(api,db,keywords,boxes)
#TwitterStream.filter_stream(api,keywords,boxes)
=======
##TwitterStream.filter_stream(api,db,keywords,boxes)
TwitterStream.filter_stream(api,keywords,boxes)
>>>>>>> a7df4af94c4ea876a69ebfde089d779b8f2dc27c:harvester/twitterHarverster.py
