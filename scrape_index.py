"""
Scrape the index page to login
"""
import sys
import platform
import requests

from models.index import IndexPage
from datetime import datetime
from utils import eprint
from selenium import webdriver

FNB_LOGIN_URL = 'https://www.fnb.co.za/'

if platform.system() == 'Windows':
	PHANTOMJS_PATH = './phantomjs.exe'
else:
	PHANTOMJS_PATH = './phantomjs'

def scrape_index():
	response = requests.get(FNB_LOGIN_URL)
	eprint('{0} [{1}]'.format(response.url, response.status_code))

	browser = webdriver.PhantomJS(PHANTOMJS_PATH)
	browser.get(FNB_LOGIN_URL)
	page = IndexPage(browser.page_source)

	#response = requests.get(FNB_LOGIN_URL)
	#eprint('{0} [{1}]'.format(response.url, response.status_code))
	#page = IndexPage(response.content)

	if not len(page.items):
		return

	for item in page.items:
		print(item.prettify())

if __name__ == '__main__':
	scrape_index()