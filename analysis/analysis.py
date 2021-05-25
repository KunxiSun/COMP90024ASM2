import couchdb
from textblob import TextBlob
import matplotlib.pylab as plt
import matplotlib.pyplot as mp
import numpy as np
import os
import json


def twitter_analysis(Master_node, database_in, year_in, update):
    # Connect to couchDB
    # Master_node = "172.26.130.11"
    couch = couchdb.Server("http://admin:admin@" + Master_node + ":5984")

    database_list = [database_in]
    year_list = [year_in]
    if database_in == "allcity":
        database_list = ["arch_syd", "arch_melb", "arch_ade", "arch_pth", "arch_bris"]
    if year_in == "allyear":
        year_list = ["2016", "2017", "2018", "2019", "2020", "2021"]

    # result dict
    result_dict = {}

    for database in database_list:
        database_dict = {}
        for year in year_list:
            # Load data from couchDB
            db = couch[database]
            print("database: ", database, "year: ", year)

            work = ["employ", "unemploy"]
            marrital = "wedding"
            pets = ["pet", "dog", "cat"]


            map_work1 = """
                        function(doc) {
                            if (doc.time.substr(0,4) == """ + year + """ && (doc.post_text).search(/""" + work[0] + """/i) >= 0)
                                emit(doc.time,[doc.post_text]);
                        }
                      """
            map_work2 = """
                        function(doc) {
                            if (doc.time.substr(0,4) == """ + year + """ && (doc.post_text).search(/""" + work[1] + """/i) >= 0)
                                emit(doc.time,[doc.post_text]);
                        }
                      """
            map_marrital = """
                        function(doc) {
                            if (doc.time.substr(0,4) == """ + year + """ && (doc.post_text).search(/""" + marrital + """/i) >= 0)
                                emit(doc.time,1);
                        }
                      """
            map_pets = """
                        function(doc) {
                            if (doc.time.substr(0,4) == """ + year + """ && 
                            ((doc.post_text).search(/""" + pets[0] + """/i) >= 0
                            || (doc.post_text).search(/""" + pets[1] + """/i) >= 0
                            || (doc.post_text).search(/""" + pets[2] + """/i) >= 0))
                                emit(doc.time,1);
                        }
                      """

            reduce_fun = "_count"

            design = {'views': {
                'get_'+work[0]+'_'+year: {
                    'map': map_work1,
                    'reduce': reduce_fun
                },
                'get_' + work[1] + '_' + year: {
                    'map': map_work2,
                    'reduce': reduce_fun
                },
                'get_marrital_' + year: {
                    'map': map_marrital,
                    'reduce': reduce_fun
                },
                'get_pets_' + year: {
                    'map': map_pets,
                    'reduce': reduce_fun
                }

            }}

            if update:
                try:
                    del(db["_design/search"+year])
                except:
                    pass

                db["_design/search"+year] = design


            map_fun = """
                        function(doc) {
                            if (doc.time.substr(0,4) == """ + year + """)
                                emit(doc.time,1);
                        }
                      """
            reduce_fun = "_count"

            design = {'views': {
                'get_year_cnt'+year: {
                    'map': map_fun,
                    'reduce': reduce_fun
                }
            }}

            if update:
                try:
                    del(db["_design/year_cnt"+year])
                except:
                    pass

                db["_design/year_cnt"+year] = design


            if not update:
                # total tweet number of this year
                total_tweet = -1
                year_cnt_list = db.view('year_cnt'+year+'/get_year_cnt'+year, reduce=True)
                for r in year_cnt_list:
                    total_tweet = r.value

                work1_list = db.view('search'+year+'/get_'+work[0]+'_'+year, reduce=False)
                employ_cnt = len(work1_list)

                work2_list = db.view('search'+year+'/get_'+work[1]+'_'+year, reduce=False)
                unemploy_cnt = len(work2_list)

                marrital_cnt_list = db.view('search'+year+'/get_marrital_'+year, reduce=True)
                for r in marrital_cnt_list:
                    marrital_cnt = r.value

                pets_cnt_list = db.view('search'+year+'/get_pets_'+year, reduce=True)
                for r in pets_cnt_list:
                    pets_cnt = r.value

                database_dict[year] = {"employ_cnt": employ_cnt, "employ_ratio": round(employ_cnt/total_tweet*100,4),
                                   "unemploy_cnt": unemploy_cnt, "unemploy_ratio": round(unemploy_cnt/total_tweet*100,4),
                                   "marrital_cnt": marrital_cnt, "marrital_ratio": round(marrital_cnt/total_tweet*100,4),
                                   "pets_cnt": pets_cnt, "pets_ratio": round(pets_cnt/total_tweet*100,4)}
        if not update:
            result_dict[database] = database_dict
    if not update:
        print(result_dict)

        output_dir = "analysis_result"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        fw = open(output_dir + "/wordfrequency-" + database_in +'-'+ year_in + ".json", 'w', encoding='utf-8')
        json.dump(result_dict, fw)
        fw.close()

        try:
            del (couch["wordfrequency-" + database_in +'-'+ year_in])
        except:
            pass
        new_db = couch.create("wordfrequency-" + database_in +'-'+ year_in)
        new_db.save(result_dict)


def SentimentAnalysis(Master_node, database_in, year_in):
    # Connect to couchDB
    # Master_node = "172.26.130.11"
    couch = couchdb.Server("http://admin:admin@" + Master_node + ":5984")

    database_list = [database_in]
    year_list = [year_in]
    if database_in == "allcity":
        database_list = ["arch_syd", "arch_melb", "arch_ade", "arch_pth", "arch_bris"]
    if year_in == "allyear":
        year_list = ["2019", "2020", "2021"]
    work = "employ"

    # result dict
    result_dict = {}

    for database in database_list:
        database_dict = {}
        for year in year_list:
            # Load data from couchDB
            db = couch[database]
            print("database: ", database, "year: ", year)
            work1_list = db.view('search' + year + '/get_' + work + '_' + year, reduce=False)


            # load tweets related to employ
            cands = []
            for r in work1_list:
                cands.append(r.value[0])
            print("total tweets:", len(cands))

            pos, neg = 0,0
            TBscore = []
            for sen in cands:
                analysis = TextBlob(sen[:-1])
                TBscore.append(round(analysis.sentiment[0],4))
                if analysis.sentiment[0] > 0:
                    pos += 1
                elif analysis.sentiment[0] < 0:
                    neg += 1

            curr_dict = {"pos": pos, "neg": neg, "avg": round(sum(TBscore) / len(TBscore),4)}
            print(curr_dict)

            database_dict[year] = curr_dict
        print(database_dict)
        result_dict[database] = database_dict
    print(result_dict)

    output_dir = "analysis_result"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    fw = open(output_dir+"/sa-employ-"+database_in+'-'+year_in+".json", 'w', encoding='utf-8')
    json.dump(result_dict, fw)
    fw.close()

    try:
        del (couch["sa-employ-"+database_in+'-'+year_in])
    except:
        pass
    new_db = couch.create("sa-employ-"+database_in+'-'+year_in)
    new_db.save(result_dict)


def AURIN_analysis(Master_node, database_in):
    # Connect to couchDB
    # Master_node = "172.26.130.11"
    couch = couchdb.Server("http://admin:admin@" + Master_node + ":5984")

    database_list = [database_in]
    if database_in == "allcity":
        database_list = ["arch_syd", "arch_melb", "arch_ade", "arch_pth", "arch_bris"]

    work = ["employ", "unemploy"]
    # result dict
    AURIN_result_dict = {}
    twitter_result_dict = {}

    for database in database_list:
        # Load data from couchDB
        db = couch[database]
        print("database: ", database)

        AURIN_database_dict = {}
        twitter_database_dict = {}


        AURIN_db = couch["unemployment_status"]

        for i in AURIN_db:
            load_dict = AURIN_db[i]
            print(AURIN_db[i]['arch_melb'])
            break

        AURIN_years = ["_16","_17","_18","_19","_20"]
        value = []
        AURIN_sum = []
        for AURIN_year in AURIN_years:
            AURIN_year_sum = 0
            for k,v in load_dict[database].items():
                if AURIN_year in k[-4:]:
                    print(k,v)
                    try:
                        value.append(int(v))
                        AURIN_year_sum += int(v)
                    except:
                        value.append(0)
                        AURIN_year_sum += 0
            AURIN_sum.append(AURIN_year_sum)
        print(value)
        AURIN_sum[-1] = AURIN_sum[-1]*2
        print(AURIN_sum)


        twitter_years = ["2016", "2017", "2018", "2019", "2020"]
        twitter_sum = []
        for twitter_year in twitter_years:
            # load twitter data from couchdb
            year_cnt_list = db.view('year_cnt' + twitter_year + '/get_year_cnt' + twitter_year, reduce=True)
            for r in year_cnt_list:
                total_tweet = r.value
                print("total: ", total_tweet)

            employ_list = db.view('search' + twitter_year + '/get_employ_' + twitter_year, reduce=False)
            employ_cnt = len(employ_list)
            print(work[0], employ_cnt, employ_cnt / total_tweet)
            twitter_sum.append(round(employ_cnt / total_tweet * 100, 4))
        print(twitter_sum)

        for i in range(len(AURIN_sum)):
            AURIN_database_dict[twitter_years[i]] = {"AURIN_data": AURIN_sum[i]}
            twitter_database_dict[twitter_years[i]] = {"twitter_data": twitter_sum[i]}
        AURIN_result_dict[database] = AURIN_database_dict
        twitter_result_dict[database] = twitter_database_dict

        fig, ax1 = plt.subplots()
        ax1.plot(twitter_years, AURIN_sum, 'o-', c='orangered', label='AURIN_data')
        mp.legend(loc=2)
        ax2 = ax1.twinx()
        ax2.plot(twitter_years, twitter_sum, 'o-', c='blue', label='Twitter_data')
        mp.legend(loc=1)
        ax1.set_xlabel("year")
        ax1.set_ylabel("Count(person)")
        ax2.set_ylabel("Frequency(%)")
        plt.title("AURIN and Twitter unemployment data from 2016 to 2020 - "+database)
        mp.gcf().autofmt_xdate()
        # plt.show()

        graph_dir = "graph"
        if not os.path.exists(graph_dir):
            os.makedirs(graph_dir)
        plt.savefig(graph_dir+'/'+"AURIN-Twitter_comparison"+database+".png")
        plt.clf()

        plt.plot(AURIN_sum, twitter_sum, 'o-')
        for i in range(len(AURIN_sum)):
            plt.text(AURIN_sum[i],twitter_sum[i],twitter_years[i])
        plt.xlabel("unemployment data on AURIN")
        plt.ylabel('frequency of word "unemploy" mentioned on Twitter')
        plt.title("AURIN-Twitter unemployment data relationship - "+database)
        # plt.show()
        plt.savefig(graph_dir+'/'+"AURIN-Twitter_relationship"+database+".png")
        plt.clf()

    # write result in json file
    output_dir = "analysis_result"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    fw = open(output_dir+"/aurin-employ-"+database_in+".json", 'w', encoding='utf-8')
    json.dump(AURIN_result_dict, fw)
    fw.close()
    fw = open(output_dir+"/twitter-employ-"+database_in+".json", 'w', encoding='utf-8')
    json.dump(twitter_result_dict, fw)
    fw.close()

    try:
        del (couch["aurin-employ-"+database_in])
    except:
        pass
    try:
        del (couch["twitter-employ-"+database_in])
    except:
        pass
    new_db = couch.create("aurin-employ-"+database_in)
    new_db.save(AURIN_result_dict)
    new_db = couch.create("twitter-employ-"+database_in)
    new_db.save(twitter_result_dict)



# create views for each year
# "arch_syd"  "arch_ade"  "arch_bris"  "arch_pth"
# for year in ["2016", "2017", "2018", "2019", "2020", "2021"]:
#     twitter_analysis("172.26.130.11","arch_melb",year,update=True)


# view results for each year
# database list: "arch_syd", "arch_melb", "arch_ade", "arch_pth", "arch_bris"
# ("172.26.130.11","arch_syd","2020",update=False)
# twitter_analysis("172.26.130.11","allcity","allyear",update=False)


# Sentiment Analysis of keyword "employ". Data stored in /SA_data and histogram stored in /graph
# ("172.26.130.11","arch_syd","2020")
# SentimentAnalysis("172.26.130.11","allcity","allyear")
# twitter_analysis("172.26.130.11","allcity","allyear",update=False)
# AURIN_analysis("172.26.130.11","allcity")
# AURIN analysis on unemployment
# AURIN_analysis("172.26.130.11","arch_ade")
# AURIN_analysis("172.26.130.11","allcity")