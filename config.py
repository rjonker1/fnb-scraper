"""
Configuration File
"""

import sys
import platform

FNB_URL = 'https://www.fnb.co.za/'

if platform.system() == 'Windows':
	PHANTOMJS_PATH = './phantomjs.exe'
else:
	PHANTOMJS_PATH = './phantomjs'