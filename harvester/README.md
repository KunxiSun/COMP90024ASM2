## Twitter Harvester

### run
python3 ./src/main.py
### Dependency
tweepy        
couchdb        
TwitterAPI        
urllib        
twarc2         
### File
config.py: Configuration Environment       
tweet_streaming.py: Use Streaming get tweets      
tweet_searcher.py: Use search get tweets      
tweet_cleaner.py: Simple clean the raw response            
tweet_arch_searcher.py: Full archive searching 
analyser.py: Connect to Back-end Analysis
main: Multithreading Run
### Output
Id: tweet id     
user_id     
post_text     
time: created time     
user_location     
location: tweet location     
location_fullname     
coordinates: tweet coordinates if exists     
hashtags: hashtags["text"], hashtages["indices"]     
### [Reference link]: 
https://developer.twitter.com/en/docs/twitter-api/premium/data-dictionary/object-model/entities#hashtags
Tweet hashtags
https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet 
tweet object standard v1     
https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet
tweet object v2      
https://twittercommunity.com/t/introducing-the-new-academic-research-product-track/148632
Full archive query      
https://pypi.org/project/TwitterAPI/
TwitterApi for tweet api v1 wrapper     
https://docs.tweepy.org/en/latest/index.html
Tweepy for tweet api v1 wrapper     
https://twarc-project.readthedocs.io/en/latest/api/client2/
Tweet api v2 wrapper     
