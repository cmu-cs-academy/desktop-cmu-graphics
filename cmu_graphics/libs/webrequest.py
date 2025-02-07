### ZIPFILE VERSION ###
from . import certifi
### END ZIPFILE VERSION ###
### PYPI VERSION ###
import certifi
### END PYPI VERSION ###

import ssl
import sys
import urllib.request

def get(path):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		   'Accept-Encoding': 'none',
		   'Accept-Language': 'en-US,en;q=0.8',
		   'Connection': 'keep-alive'
	}
	request = urllib.request.Request(path, headers=headers)
	if sys.version_info >= (3, 13):
		context = ssl.create_default_context(cafile=certifi.where())
		response = urllib.request.urlopen(request, context=context)
	else:
		response = urllib.request.urlopen(request, cafile=certifi.where())
	return response

