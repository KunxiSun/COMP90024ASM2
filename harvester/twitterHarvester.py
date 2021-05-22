from TwitterAPI import TwitterAPI
import TwitterStream
import couchdb 
import config


def main():
    #load variables from config
    keywords = config.keywords
    boxes = config.box_melb
    #boxes = config.melbourne_city

    #connect to db server
    couch = couchdb.Server(config.couchdb_url)

    #connect to database
    db = couch[config.couchdb_name]

    #create TwitterAPI object
    api = TwitterAPI(config.consumer_key,
                    config.consumer_secret,
                    config.access_token,
                    config.access_token_secret)
    TwitterStream.filter_stream(api,db,keywords,boxes)

if __name__ == "__main__":
    main()


