import sys
import time
from selenium import webdriver

class LoginPage:	
	def __init__(self, browser):		
		self._browser = browser
		self.statusCode = 404
		#self._clearTextboxes()

	def _clearTextboxes(self):
		self._browser.find_element_by_id('user').clear()
		self._browser.find_element_by_id('pass').clear()

	def Login(self):
		self._browser.find_element_by_id('user').send_keys('########')
		self._browser.find_element_by_id('pass').send_keys('########')
		self._browser.find_element_by_id('OBSubmit').click()
		time.sleep(10)
		return self._browser.current_url

	def Logout(self):
		print('Logging out')
		logoutButton = self._browser.find_element_by_xpath('//div[@id="headerButton_1]/a"')
		logoutButton.click()