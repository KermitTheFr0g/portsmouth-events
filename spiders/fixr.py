import logging
import time

import requests
from bs4 import BeautifulSoup

from base_spider.spider import BaseSpider

class FixrCrawler(BaseSpider):
    NAME = "Fixr"
    ALLOWED_DOMAINS = ['']
    BASE_URL = f""
    HEADERS = {
        "accept": "application/json; version=3.0",
        "accept-language": "en-GB",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "fixr-app-version": "7.51.7",
        "fixr-channel": "fixr-website",
        "fixr-channel-meta": "e30=",
        "fixr-platform": "web",
        "fixr-platform-version": "Chrome/141.0.0.0",
        "fixr-tracking": '{"utm_source":"chatgpt.com"}',
        "origin": "https://fixr.co",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://fixr.co/",
        "sec-ch-ua": '"Brave";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
        "user-agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/141.0.0.0 Safari/537.36"
        ),
    }
    
    def __init__(self):
        self.session = requests.Session()
        super().__init__(self.NAME, self.session)
        
    def crawl(self):
        response = self.session.get("https://fixr.co/", headers=self.HEADERS)
        print(response)
        response = self.fetch("https://api.fixr.co/search/events?query=&lat=50.8197675&lon=-1.0879769&sold_out=true&limit=12&offset=0&radius=25&ordering=opens_at_decay&location__decay_function__offset=25km&popularity__boost=0")
        print(response)
    
fixr_crawler = FixrCrawler()
fixr_crawler.crawl()
