import requests
import re
from links_crw import *
import concurrent.futures

def emailfinder(url) :
	emails=SearchWeb(url,"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
	print('\n'.join(emails))
	return emails

def phonenumberfinder(url) :
	phonenumbers = SearchWeb(url,"(\(\+?[0-9]+\).[0-9]+.[0-9]+.[0-9]+)")
	print("\n".join(phonenumbers))
	return phonenumbers


def SearchWeb(url,RegEx) :
	r=requests.Session()
	try :
		s = r.get(url)
		return re.findall(RegEx,s.text)
	except Exception :
		return [] 