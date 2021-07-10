from bs4 import BeautifulSoup
import requests
import re
import sys



def getlinks(url):
	
	r=requests.Session()
	s = r.get(url)
	soup = BeautifulSoup(s.text, 'html.parser')
	links=[]	

	print('\n')
	for link in soup.find_all('a') :
		try :
			if '?' in link.get('href') :
				continue
			if (link.get('href')[:7]=='http://') or (link.get('href')[:8]=='https://') :
				
				print('\33[95m'+link.get('href'))
				
			else :
				a=link.get('href')[1:] if link.get('href')[0]=='/' else link.get('href')
				
				print('\33[95m'+url+'/'+a)
	
		except :
			continue

	print('\n')