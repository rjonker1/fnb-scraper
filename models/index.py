from bs4 import BeautifulSoup
from dateutil.parser import parser

class IndexPage:	
	def __init__(self, html):		
		self._html = html	
		self._soup = BeautifulSoup(self._html, 'html.parser')
		self.items = []
		self._parse()

	def _parse(self):
		container = self._soup.find('div', { id : 'whatsNewContainer' })		
		if container:
			links = container.find('ul')
			for link in links:
				self.items.append(link)