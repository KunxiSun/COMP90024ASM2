### run
python3 ./src/main.py

### Dependency
tweepy
couchdb
TwitterAPI
#### File
Configuration Environment in config.py \\
Use Streaming get tweets in TwitterStream.py\\
Full archive searching in tweet_arch_searcher.py\\

#### Output

Id: tweet id

user_id

post_text

time: created time

user_location

location: tweet location

location_fullname

coordinates: tweet coordinates if exists

hashtags: hashtags["text"], hashtages["indices"]

[Reference link]: https://developer.twitter.com/en/docs/twitter-api/premium/data-dictionary/object-model/entities#hashtags

