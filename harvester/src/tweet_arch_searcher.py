
#reference : https://pydigger.com/pypi/twarc
#https://twittercommunity.com/t/help-with-full-archive-search-with-tweepy-or-easy-python-alternative/153360/4
#from harvester.src.analyser import analyser

from couchdb.client import Server
from datetime import datetime
#from analyser import Analyser
from twarc.client2 import Twarc2
from twarc.expansions import flatten
import couchdb
import config
import urllib.parse
import base64
import requests
import threading

def get_bearer_token(consumer_key, consumer_secret):
    # encode consumer key
    consumer_key = urllib.parse.quote(consumer_key)
    # encode consumer secret
    consumer_secret = urllib.parse.quote(consumer_secret)
    # create bearer token
    bearer_token = consumer_key + ':' + consumer_secret
    # base64 encode the token
    base64_encoded_bearer_token = base64.b64encode(bearer_token.encode('utf-8'))
    # set headers
    headers = {
        "Authorization": "Basic " + base64_encoded_bearer_token.decode('utf-8') + "",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Content-Length": "29"}
    response = requests.post(OAUTH2_TOKEN, headers=headers, data={'grant_type': 'client_credentials'})
    to_json = response.json()
    bearer_token = to_json['access_token']
    return bearer_token

def crawl_data(year,month,start_day,province,geo,db,twarc2):
    
    # Start and end times must be in UTC
    start_time = datetime.datetime(year, month, start_day, 0, 0, 0, 0, datetime.timezone.utc)
    end_time = datetime.datetime(year, month, int(start_day)+1, 0, 0, 0, 0, datetime.timezone.utc)
    # search_results is a generator, max_results is max tweets per page
    search_results = twarc2.search_all(query=f'-is:retweet point_radius:{geo}', start_time=start_time, end_time=end_time, max_results=100)
    # this will get all pages
    for page in search_results:
    # flatten applies to a page of results, 
    # and modifies the original response to append extra info
        expanded = flatten(page) 
        count = 0
        for tweet in expanded['data']:
            try:
                doc = clean_data(tweet,province)
                count += 1
                db.save(doc)
                if count >= 5000:
                    continue
            except couchdb.http.ResourceConflict:
                print("exists duplicate data")
                pass
    return 

def clean_data(tweet,province):
    doc = {}
    doc["_id"] = tweet["id"]
    time = tweet["created_at"]
    doc["time"] = datetime.strftime(datetime.strptime(time,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')
    doc["post_text"] = tweet["pfull_text"]
    doc['place'] = province
    print(tweet["place"]["name"])
    return doc

def connect_to_couch(db_url,dbname):
    couch = couchdb.Server(db_url)
    db = couch[dbname]
    return db

def upload_to_couch(province,geo,dbname,twarc2):   
    #connect to database 
    db = connect_to_couch(config.couchdb_url,dbname)
    for year in range(2016,2022):
        print("=====================year========================")
        for month in range(1,13):
            print("=====================month========================")
            #Take two days for the upper, middle and lower of each month
            for day in [1,10,20]:
                day = int(day)
                crawl_data(year,month,day,province,geo,db,twarc2)
        
australia = '-29.1425,133.1389,2081km'
melbourne = '-37.7867,144.9082,100km'
sydney = '-33.8813,151.2128,100km'
brisbane = '-27.5394,153.1024,100km'
adelaide = '-34.9328,138.6444,100km'
perth = '-32.0379,115.8808,100km'

provinces = ['melbourne', 'sydney', 'brisbane', 'adelaide', 'perth']
geocodes = [melbourne, sydney, brisbane, adelaide, perth]
db_name = ['arch_melb','arch_sydney','arch_bris','arch_ade','arch_pth']
print("Read coucdb ip from Ansible inventory: ",config.couchdb_ip)
print("couchdb url:", config.couchdb_url)

if __name__ == "main":
    print("Read coucdb ip from Ansible inventory: ",config.couchdb_ip)
    print("couchdb url:", config.couchdb_url)
    #connect to db server
    couch = couchdb.Server(couchdb_url) 
    #Authorization to twitter v2
    bearer_token = get_bearer_token(config.consumer_key_a,config.consumer_secret_a)
    twarc2 = Twarc2(bearer_token)
    # # run in background
    t0 = threading.Thread(target=upload_to_couch, args=('provinces[0]','geocodes[0]','db_name[0]','twarc2'), daemon=True)
    t1 = threading.Thread(target=upload_to_couch, args=('provinces[1]','geocodes[1]','db_name[1]','twarc2'), daemon=True)
    t2 = threading.Thread(target=upload_to_couch, args=('provinces[2]','geocodes[2]','db_name[2]','twarc2'), daemon=True)
    t3 = threading.Thread(target=upload_to_couch, args=('provinces[3]','geocodes[3]','db_name[3]','twarc2'), daemon=True)
    t4 = threading.Thread(target=upload_to_couch, args=('provinces[4]','geocodes[4]','db_name[4]','twarc2'), daemon=True)
    
    # starting threads 
    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
