import logging
import time
import json
import random
import urllib.parse

import requests

from base_spider.spider import BaseSpider

class VisitPortsmouthCrawler(BaseSpider):
    NAME = "VisitPortsmouth"
    ALLOWED_DOMAINS = ['www.visitportsmouth.co.uk']
    BASE_URL = f"https://{ALLOWED_DOMAINS[0]}"
    
    def __init__(self):
        self.session = requests.Session()
        super().__init__(self.NAME, self.session)
        
    def crawl(self):
        for events in self._parse_all_events():
            for event in events:
                self._parse_events_page(event)
        
    def _parse_events_page(self, event):
        # print(json.dumps(event, indent=4))
        print(event["title"])
    
    @staticmethod
    def _event_query(limit: int, skip: int) -> json:
        query = {
            "filter": {
                "active": True,
            "$and": [
                {
                    "categories.catId": {
                        "$in": [
            "10731","10741","10751","10761","10771","10781","10791","10801","10811",
            "10821","10831","10841","10851","10861","10871","10881","10891","11651",
            "11661","11671","11701","11711","11721","11731","11741","11751","11761",
            "11771","11781","11791","11801","11811","11821","11831","11841","11851",
            "11861","11871","12843","12853","13173","13413","13423","13433","13443",
            "13453","13483","13493","13503","13513","13763","14453","14903","15111",
            "15221","15481","15611","15621","15631","15721","15731","15791","15801",
            "15851","16081","16141","16331","16341","16351","16361","16371","16381",
            "16391","16401","16411","16421","16441","16461","16491","16571","16581",
            "16591","16601","16611","16631"
          ]
        }
      },
      {
        "custom.channels.channelkey": {
          "$in": [149743]
        }
      }
    ],
    "date_range": {
      "start": {"$date": "2025-10-14T23:00:00.000Z"},
      "end": {"$date": "2025-11-15T00:00:00.000Z"}
    }
  },
  "options": {
    "limit": limit,
    "skip": skip,
    "count": True,
    "castDocs": True,
    "fields": {
      "_id":1,"location":1,"udfs_object.24.value_raw":1,"udfs_object.25.value_raw":1,
      "udfs_object.20.value_raw":1,"udfs_object.21.value_raw":1,"udfs_object.18.value_raw":1,
      "udfs_object.19.value_raw":1,"date":1,"startDate":1,"endDate":1,"recurrence":1,
      "recurType":1,"latitude":1,"longitude":1,"media_raw":1,"recid":1,"type":1,"dates":1,
      "title":1,"url":1,"accountId":1,"city":1,"region":1,"udfs_object.20.value_string":1,
      "udfs_object.17.value_raw":1,"udfs_object.26.value_string":1,
      "udfs.find(udfs => udfs.fieldid===24).value":1,
      "udfs.find(udfs => udfs.fieldid===25).value":1,
      "listing.title":1,"listing.url":1,"listing.recid":1,"listing.acctid":1,"listing.region":1,
      "listing.city":1,"listing.primary_category":1,"listing.rankname":1,"listing.custom.price":1,
      "udfs_object.2.value":1,"custom.rankid":1,"custom.channels.channelkey":1,
      "custom.rankname":1,"custom.price":1,"custom.city":1,"categories":1
    },
    "hooks": [],
    "sort": {"date":1,"rank":1,"udfs_object.15.value":1,"title_sort":1}
  }
} 
        return query
        
    def _parse_all_events(self):    
        page_size = 15
        skip = 0
        doc_amount = None
        
        while True:
            query = self._event_query(page_size, skip)
            encoded_query = urllib.parse.quote(json.dumps(query))
            url = f"{self.BASE_URL}/includes/rest_v2/plugins_events_events_by_date/find/?json={encoded_query}&token=adefb5507e6ca1d2bb0d62283e5a2a7c"
            response = self.fetch(url)
            events = response['docs']['docs']
            if doc_amount is None:
                doc_amount = response["docs"]["count"]
            skip += page_size
            if events is None:
                break
            yield events
            if skip >= doc_amount:
                break
            
            sleep_amount = random.randint(3, 6)
            self.logger.info(f"Waiting for event pages sleeping for {sleep_amount} seconds.")
        
            
if __name__ == "__main__":
    visit_portsmouth = VisitPortsmouthCrawler()
    visit_portsmouth.crawl()    
