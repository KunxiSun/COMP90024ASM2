from datetime import datetime


# Given a keys(path), find the value directed to the path in a response
# Eg. Response['user']['id']
def get_data(response: str,path:list) -> str:
    r=response
    for p in path:
        if r and p in r:
            r=r[p]
        else:
            return None
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