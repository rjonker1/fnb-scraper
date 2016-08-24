"""
Scrape the index page to login
"""
import sys
import requests
import models

from models.index import IndexPage
from datetime import datetime
from utils import eprint

FNB_LOGIN_URL = 'https://www.fnb.co.za/'

def scrape_index():
	while True:
		response = requests.get(FNB_LOGIN_URL)
		eprint('{0} [{1}]'.format(response.url, response.status_code))
		page = IndexPage(response.content)
		if not len(page.items):
			break

		for item in page.items:
			print(item)

if __name__ == '__main__':
	scrape_index()