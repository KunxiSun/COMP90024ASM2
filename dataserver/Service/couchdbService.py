import couchdb

def server_connection():
    try:
        server = couchdb.Server('http://admin:admin@172.26.130.11:5984/')
        print("CouchDB is connected: " + str(server) + "\n")
        return server

    except Exception as e:
        print(e)

def get_db(server, db_name):
    try:
        db = server[db_name]
        return db
    except Exception as e:
        print(e)

server = server_connection()

# serviceImpl
def sa_employ_allcity_allyear():
    db = get_db(server,"sa-employ-allcity-allyear")
    for i in db:
        data = db[i]
        break
    data.pop('_id')
    data.pop('_rev')
    return data
    
def wordfrequency_allcity_allyear():
    db = get_db(server,"wordfrequency-allcity-allyear")
    for i in db:
        data = db[i]
        break
    data.pop('_id')
    data.pop('_rev')
    return data

def employ_allcity():
    db_aurin = get_db(server,"aurin-employ-allcity")
    db_twitter = get_db(server,"twitter-employ-allcity")
    for i in db_aurin:
        data_aurin = db_aurin[i]
        break
    for i in db_twitter:
        data_twitter = db_twitter[i]
        break
    data_aurin.pop('_id')
    data_aurin.pop('_rev')
    data_twitter.pop('_id')
    data_twitter.pop('_rev')
    ret = {}
    for zone in data_aurin:
        ret[zone] = {}
        for year in data_aurin[zone]:
            ret[zone][year] = {**data_aurin[zone][year], **data_twitter[zone][year]} 
    return ret