import base64
from couchdb.client import Server
import requests
import couchdb
import time
import sys
import tweet_cleaner

#####################################################################################

# def server_connection(id, pw, ip, port):
#     try:
#         server = couchdb.Server('http://{}:{}@{}:{}/'.format(id, pw, ip, port))
#         print("CouchDB is connected: " + str(server) + "\n")
#         return server

#     except Exception as e:
#         print(e)


# def get_db(server, db_name):
#     try:
#         db = server[db_name]
#         return db
#     except Exception as e:
#         print(e)

def print_time():
    now = time.localtime()
    print("Time: %04d/%02d/%02d %02d:%02d:%02d" % (
    now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))


def search_tweets(query, provinces, geocodes, since, until, db, base_url, search_headers):
    for idx, province in enumerate(provinces):
        # initial start id
        since_id = 9999999999999999999999999999999999

        geocode = geocodes[idx]

        while True:
            try:
                search_params = {
                    'q': '{}'.format(query),
                    'geocode': '{}'.format(geocode),
                    'since': '{}'.format(since),  # only 7 days before
                    'until': '{}'.format(until),
                    'count': 100,  # max 100 with free api
                    'result_type': 'recent',  # mixed, recent, popular
                    'max_id': '{}'.format(str(since_id)),
                    'retryonratelimit': True
                }

                search_url = '{}1.1/search/tweets.json'.format(base_url)
                search_resp = requests.get(search_url, headers=search_headers, params=search_params)
                tweet_data = search_resp.json()['statuses']

                if len(tweet_data) != 0:
                    for tweet in tweet_data:

                        try:
                            since_id = tweet["id"]
                            tweet["_id"] = tweet["id_str"]

                            doc=tweet_cleaner.get_result(tweet)

                            # if processed data is not ideal, continue
                            if not doc:                 
                                print ("didn't get ideal response, try again")
                                continue 

                            # Invoke Li yi's code to analysis new tweet: doc
                            db.save(doc)
                            print("Search:%s\n"%(doc))

                            #print("Tweet is collected [ {}_radius ]> {}\n".format(province, tweet["_id"]))

                        except Exception as e_db:
                            continue
                            # print(str(e_db) + "\n")

                    since_id = since_id - 1

                else:
                    print("Tweets about the requested query does not exist\n")
                    break
            
            except Exception as e:
                print_time()
                print(e)

                print("\nAPI reaches the rating limit, Sleep 15 min\n")
                time.sleep(930)  # sleep 15min 30sec

