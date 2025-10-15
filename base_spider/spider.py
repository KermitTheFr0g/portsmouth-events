import logging
import json

import requests
from bs4 import BeautifulSoup

class BaseSpider(object):
    """Base spider object for all crawlers to inherit."""
    
    def __init__(self, name, session : requests.Session):
        self.NAME = name
        self.ES = None
        self.logger = None
        self._session = session
        
        self.__initalise_logger()
        
    def __initalise_logger(self):
        self.logger = logging.getLogger(self.NAME)
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler('crawlers.log', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def upload_to_es(self, data):
        pass
    
    def fetch_soup(self, url) -> BeautifulSoup: 
        response = self._session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup
    
    def fetch(self, url: str):
        self.logger.info(f"Making GET request to: {url}")
        response = self._session.get(url)   
        return response.json()
    