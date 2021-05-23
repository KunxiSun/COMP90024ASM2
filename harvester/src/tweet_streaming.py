import TwitterAPI
import couchdb
import time
import tweet_cleaner


# Use filter stream select location
def filter_stream(api,db,keywords,boxes):
        
    #construct the request to twitter
    request_map={'locations': boxes,"lang": "en","retweeted":"false", 'track':""}

    #track_term delimited by ","
    TRACK_TERM=",".join(keywords)

    # Store the track term in request map
    if TRACK_TERM=="":
        print("Sreaming: Filtering without keywords")
    else:
        request_map['track']=TRACK_TERM
    while 1:
        try:
            responses = api.request('statuses/filter', request_map)
            for response in responses:
                # use dict doc to store results
                doc=tweet_cleaner.get_result(response)

                # if processed data is not ideal, continue
                if not doc:                 
                    print ("didn't get ideal response, try again")
                    continue 

                # Invoke Li yi's code to analysis new tweet: doc
                
                db.save(doc)
                print("Streaming:%s\n"%(doc))

        # Ignore the existence of the same id
        # Due to limit speed to harvest tweets, program has to sleep for a while
        # when encouter errors
        except couchdb.http.ResourceConflict:
            pass
        except TwitterAPI.TwitterError.TwitterRequestError as e:
            time.sleep(60*15)
            if e.status_code < 500:
                raise
            else:
                pass
        except TwitterAPI.TwitterError.TwitterConnectionError:
            time.sleep(60*15)
            pass
        