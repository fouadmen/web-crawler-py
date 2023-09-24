from bs4 import BeautifulSoup

import requests
from requests.exceptions import RequestException
import sys
import os


class Fetch():

    def fetch_url(self, url):
        try:
            res = requests.get(url)
            if res.status_code == 200:
                return BeautifulSoup(res.text, features="html.parser")
            else:
                raise ValueError("Page not found")
        except RequestException as e:
            print(e)
            sys.exit(1)
