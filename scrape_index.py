"""
Login and scrape the index page
"""
import sys
import platform
import requests

from config import *
from models.index import IndexPage
from models.login import LoginPage
from datetime import datetime
from utils import eprint
from selenium import webdriver

def scrape_index():
	response = requests.get(FNB_URL)
	eprint('{0} [{1}]'.format(response.url, response.status_code))
	browser = webdriver.PhantomJS(PHANTOMJS_PATH, service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
	browser.set_window_size(1120, 550)
	browser.get(FNB_URL)

	loginPage = LoginPage(browser)
	loginPage.Login()

	print(browser.current_url)

	#browser.get(browser.current_url)
	page = IndexPage(browser.page_source)

	if not len(page.items):
		print('login failed!')

	for item in page.items:
		print(item.prettify())

	loginPage.Logout()

if __name__ == '__main__':	
	scrape_index()