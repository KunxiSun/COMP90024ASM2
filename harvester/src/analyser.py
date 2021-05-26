import config
import sys
import time
import sys
sys.path.append("analysis")
import analysis

class Analyser:
    def run(self, doc, count):
        if count%config.update_view_count!=0:
            return 
        if doc == None:
            return 
            
        # update views
        #print(doc)
        couchdb_ip = config.get_couchdb_ip()

        dbname = self._get_dbname_by_location(doc)
        year = self._get_year_by_time(doc)
        print("check name",year, dbname)
        analysis.twitter_analysis(couchdb_ip, dbname, year, update=True)
        

        # sleep 25 min to wait views in couchdb are updated
        time.sleep(25*60)

        # analysis
        analysis.twitter_analysis(couchdb_ip,"allcity","allyear",update=False)
        analysis.SentimentAnalysis(couchdb_ip,"allcity","allyear")
        analysis.AURIN_analysis(couchdb_ip,"allcity")

    def _get_dbname_by_location(self, doc):
        if doc == None:
            return None

        place = doc["user_location"].split(",")[0]
        if  place == "Brisbane":
            return "arch_bris"
        elif place == "Adelaide":
            return "arch_ade"
        elif place == "Perth":
            return "arch_pth"
        elif place == "Melbourne":
            return "arch_melb"
        elif place == "Sydney":
            return "arch_syd"
        else:
            return None

    def _get_year_by_time(self, doc):
        time = doc["time"]
        time = time.split(' ')[0]
        time = time.split('-')[0]
        return time

    

