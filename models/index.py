from bs4 import BeautifulSoup
from dateutil.parser import parser

#, stop_datetime

FNB_URL = 'https://www.fnb.co.za/'

class IndexPage:	
	def __init__(self, html):		
		self._html = html
		# self._stop_datetime = stop_datetime
		self._soup = BeautifulSoup(self._html, 'html.parser')
		self.items = []
		self._parse()

	def _parse(self):
		container = self._soup.find(class='loginFields')
		if container:
			divs = container.find_all('div')
			for elment in divs:
				self.items.append(elments)		