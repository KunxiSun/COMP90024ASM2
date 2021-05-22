import TwitterAPI
import couchdb
from datetime import datetime
import time
import json
#before get the value, check not none
#get doc["place"]["name"]
#check doc["place"] is not none
def get_data(response: str,path:list) -> str:
    r=response
    for p in path:
        if r and p in r:
            r=r[p]
        else:
            return None
    return r

#Check if the key of dict doc has a value
#such as place, coordinates
def check_none(doc: dict, key: str, value: str):
    if value:
        doc[key]=value
    else: doc[key]=None

#build a dict doc for upload to couchdb later
#contains: _id, user_id, post_text, location, location_fullname, coodinates
def get_result(response: dict) -> dict:
    
    doc = dict()
    doc["_id"] = str(response["id"])
    #print(doc["_id"],'doc["_id"]')
    d=get_data(response,["user","id"])
    doc["user_id"] = d
    doc["post_text"] = response['text']
    doc["time"] = new_datetime = datetime.strftime(datetime.strptime(response["created_at"],
            '%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')
    check_none(doc,"user_location", get_data(response,["user","location"]))
    check_none(doc,"location", get_data(response,["place","name"]) )
    check_none(doc,"location_fullname", get_data(response,["place","full_name"]))
    check_none(doc,"coordinates",get_data(response,["coordinates","coordinates"]))
    check_none(doc,"hashtags",get_data(response,["entities","hashtags"]))
    return doc

def write_json(json_str):
    with open('melb_json.json','a+') as f:
        f.write(json_str)



#use filter stream select location
##def filter_stream(api,db,keywords,boxes):
def filter_stream(api,keywords,boxes):
    count=0
    #track_term delimited by ","
    TRACK_TERM=",".join(keywords)
    #construct the request to twitter
    request_map={'locations': boxes,"lang": "en","retweeted":"false"}
    if TRACK_TERM=="":
        print("filter without keyword")
    else:
        #if the keywords are not empty, set it in the request
        request_map['track']=TRACK_TERM
    while 1:
        try:
            r = api.request('statuses/filter', request_map)
            for response in r:
                #use dict doc to store results
                doc=get_result(response)
                if not doc:                 
                    print ("didn't get ideal response, try again")
                    continue 
                json_doc = json.dumps(doc)          
                
                write_json(json_doc)
                ##db.save(doc)
                count+=1
                if count==1:
                    break
                    #print(doc)
                if count % 100 ==0:
                    print (count)
        #Ignore the existence of the same id
        ##except couchdb.http.ResourceConflict:
        ##    pass
        except TwitterAPI.TwitterError.TwitterRequestError as e:
            if e.status_code < 500:
                time.sleep(60)
                raise
            else:
                time.sleep(60)
                pass
        except TwitterAPI.TwitterError.TwitterConnectionError:
            time.sleep(60)
            pass
        



