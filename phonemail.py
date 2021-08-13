import requests
import re
from links_crw import *

def emailfinder(url) :
	r=requests.Session()
	s = r.get(url)
	return re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",s.text) 

def phonenumberfinder(url) :
	r=requests.Session()
	s = r.get(url)
	return re.findall("(\(\+?[0-9]+\).[0-9]+.[0-9]+.[0-9]+)",s.text)

def emailcol(url) :
	emails=set()
	for i in linkcrawl(url)[0] :
		for j in emailfinder(i) :
			if j in emails :
				continue
			emails.add(j)
			print(j)
	return emails

def phonenumbercol(url) :
	phonenumbers=set()
	for i in linkcrawl(url)[0] :
		for j in phonenumberfinder(i) :
			if j in phonenumbers :
				continue
			phonenumbers.add(j)
			print(j)
	return phonenumbers