import config
import sys
import time
import sys
sys.path.append("../../analysis")
import analysis

class Analyser:
    def run(self, doc, count):
        if count%10000!=0:
            return 
            
        # update views
        dbname = self._get_dbname_by_location(doc)
        year = self._get_year_by_time(doc)
        analysis.twitter_analysis(config.couchdb_ip, dbname, year, update=True)

        # sleep 25 min to wait views in couchdb are updated
        time.sleep(25*60)

        # analysis
        analysis.twitter_analysis(config.couchdb_ip,"allcity","allyear",update=False)
        analysis.SentimentAnalysis(config.couchdb_ip,"allcity","allyear")
        analysis.AURIN_analysis(config.couchdb_ip,"allcity")

    def _get_dbname_by_location(doc):
        place = doc["place"]
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

    def _get_year_by_time(doc):
        time = doc[time]
        time = time.split(' ')[0]
        time = time.split('-')[0]
        return time

    

