import json
import couchdb

db_url = "http://admin:admin@172.26.130.11:5984" 

#connect to db server
couch = couchdb.Server(db_url)
#connect to database
db = couch['aurin_unemployment2010-2020']
print(db)

#create TwitterAPI object
with open('./aurin/Smoothed_Unemployment_2010-2020.json', 'r', encoding="utf-8") as f:
    # 读取所有行 每行会是一个字符串
    for jsonstr in f.readlines():
        # 将josn字符串转化为dict字典
        jsonstr = json.loads(jsonstr)
        #tweet_id = jsonstr["id"]
        try:
            print(jsonstr)
            #if tweet_id in db:
            #    print("tweet_id",tweet_id,"already in database")
            #else:
            #db.save(jsonstr)
        except couchdb.http.ResourceConflict:
            print("exists duplicate data")
            pass