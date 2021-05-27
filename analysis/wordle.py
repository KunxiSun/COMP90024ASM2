import couchdb
import re
import nltk
# nltk.download("words")
# nltk.download("punkt")
# nltk.download("wordnet")
# nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize


stopwords_path = "stopword.txt"
stopwords = []
with open(stopwords_path, 'r', encoding='utf-8') as fp:
    lines = fp.readlines()
    stopwords = [x.strip('\n') for x in lines]
fp.close()
print(stopwords[-3:])

extra_stopwords = ["good", "love", "dont", "work", "australia", "years", "week", "call", "great", "fuck", "start"
                   ,"show", "watch", "feel", "adelaide", "melbourne", "sydney", "perth", "brisbane"
                   ,"south", "north", "east", "west", "morning", "evening", "afternoon"]
stopwords += extra_stopwords

# Functions
def clean_emoji(text):
    return text.encode("ascii", "ignore").decode("ascii")


reg_map = {
    re.compile("rt [@0-9a-z_]{0,10}:"),
    re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"),
    re.compile("#[0-9a-z]+"),
    re.compile("@[0-9a-z]+"),
}


def remove_regex(text):
    text = text.lower()
    for v in reg_map:
        text = v.sub("", text)
    return text


def tokenize(text):
    return_list = []
    for word in word_tokenize(text):
        if word.isalnum() and len(word) > 2 and word not in stopwords:
            return_list.append(WordNetLemmatizer().lemmatize(word, pos="v"))
    return return_list


def pre_proccess(line):
    line = clean_emoji(line)
    line = remove_regex(line)
    words = tokenize(line)
    return list(words)


def wordle(Master_node, database_in, update):
    # Connect to couchDB
    # Master_node = "172.26.130.11"
    couch = couchdb.Server("http://admin:admin@"+Master_node+":5984")


    # Load data from couchDB
    database_list = [database_in]
    if database_in == "allcity":
        database_list = ["arch_syd", "arch_melb", "arch_ade", "arch_pth", "arch_bris"]

    for database in database_list:
        db = couch[database]

        periods = ["before", "after"]

        if update:
                map_fun1 = """
                            function(doc) {
                                if (doc.time.substr(0,4) >= "2019")
                                {
                                    emit(doc.time,[doc.post_text]);
                                }
                            }
                          """

                map_fun2 = """
                            function(doc) {
                                if (doc.time.substr(0,4) < "2019")
                                    emit(doc.time,[doc.post_text]);
                            }
                          """
                reduce_fun = "_count"

                design = {'views': {
                    'get_date_after': {
                        'map': map_fun1,
                        'reduce': reduce_fun
                    },
                    'get_date_before': {
                        'map': map_fun2,
                        'reduce': reduce_fun
                    }
                }}

                try:
                    del(db["_design/date"])
                except:
                    pass

                db["_design/date"] = design
                print(database,' established')
        else:
            for twitter_period in periods:
                output_name = "graph/"+database+"_"+twitter_period+".png"
                tweet_list = db.view('date/get_date_'+twitter_period, reduce=False)

                print(tweet_list)

                cands = []
                cnt = 0
                for r in tweet_list:
                    cands.append(r.value[0])
                    cnt += 1
                print(len(tweet_list))


                # Data preprocessing
                twitter_processed = []
                for doc in cands:
                    twitter_processed.append(pre_proccess(doc))

                print(len(twitter_processed))
                print(twitter_processed[:3])


                # Build graph
                import stylecloud
                from itertools import chain

                words = chain.from_iterable(twitter_processed)
                stylecloud.gen_stylecloud(' '.join(words),icon_name="fab fa-twitter",output_name=output_name)


# database list: "arch_syd", "arch_melb", "arch_ade", "arch_pth", "arch_bris"

# build views
# for city in ["arch_syd", "arch_melb", "arch_ade", "arch_pth", "arch_bris"]:
#     wordle("172.26.130.11", city, update=True)

# create word cloud
# for city in ["arch_syd", "arch_melb", "arch_ade", "arch_pth", "arch_bris"]:
#     wordle("172.26.130.11", city, update=False)