import TwitterAPI
import couchdb
from datetime import datetime
import time
import json
# Given a keys(path), find the value directed to the path in a response
# Eg. Response['user']['id']
def get_data(response: str,path:list) -> str:
    r=response
    for p in path:
        if r and p in r:
            r=r[p]
        else:
            return None
    print("path",path, "r",r)
    return r

# Check if the value from response is None
def check_none(value: str):
    if value:
        return value
    else: 
        return None

#build a dict doc for upload to couchdb later
#contains: _id, user_id, post_text, location, location_fullname, coodinates
def get_result(response: dict) -> dict:
    
    doc = dict()
    doc["_id"] = str(response["id"])
    doc["user_id"] = get_data(response,["user","id"])
    doc["post_text"] = response['text']
    doc["time"] = new_datetime = datetime.strftime(datetime.strptime(response["created_at"], '%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')
    doc["user_location"] = check_none(get_data(response,["user","location"]))
    doc["location"] = check_none(get_data(response,["place","name"]))
    doc["location_fullname"] = check_none(get_data(response,["place","full_name"]))
    doc["coordinates"] = check_none(get_data(response,["coordinates","coordinates"]))
    doc["hashtags"] = check_none(get_data(response,["entities","hashtags"]))

    return doc


# Use filter stream select location
def filter_stream(api,db,keywords,boxes):
        
    #construct the request to twitter
    request_map={'locations': boxes,"lang": "en","retweeted":"false", 'track':""}

    #track_term delimited by ","
    TRACK_TERM=",".join(keywords)

    # Store the track term in request map
    if TRACK_TERM=="":
        print("Filtering without keywords")
    else:
        request_map['track']=TRACK_TERM
    while 1:
        try:
            responses = api.request('statuses/filter', request_map)
            for response in responses:
                # use dict doc to store results
                doc=get_result(response)

                # if processed data is not ideal, continue
                if not doc:                 
                    print ("didn't get ideal response, try again")
                    continue 

                # Invoke Li yi's code to analysis new tweet: doc
                
                db.save(doc)
                print(doc)

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
        



