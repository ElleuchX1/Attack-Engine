import requests
from urllib.parse import urlparse ,urljoin , quote
from bs4 import BeautifulSoup

headers= {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36" , 
"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" , 
"Referer" : "http://challenge01.root-me.org/web-serveur/ch34/?action=login" , 
"Accept-Encoding" : "gzip, deflate" , 
"Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7"  }

def params(url,cookies={}) :
	try :
		domain=urlparse(url).netloc
		path=urlparse(url).path
		r = requests.get(url , cookies=cookies ,headers=headers)
		assert r.status_code==200 
		soup = BeautifulSoup(r.text, 'html.parser')
		get,post={},{}
		for link in soup.find_all("a") :
			href=link.get("href")
			if urlparse(href).netloc != '' and urlparse(href).netloc != domain   :
				continue
			if "?" in href :
				P=urlparse(href).path if urlparse(href).path != '' else	 path
				para=urlparse(href).query
				for i in para.split("&") :
					a=i[:i.index("=")] if '=' in i else i
					get[a]=P
		for form in soup.find_all("form") :
			path=str(form.get("action"))
			method=str(form.get("method"))
			soup1 = BeautifulSoup(str(form), 'html.parser')
			inputs=[]
			for inpu in soup1.find_all("input") :
				name=inpu.get('name')
				if name :
					inputs.append(name)
			if method.upper()=="GET" :
				get[tuple(inputs) if len(inputs)>1 else inputs[0]]=path

			if method.upper()=="POST" :
				post[tuple(inputs)if len(inputs)>1 else inputs[0] ]=path
		return {"get":get,"post":post}
	except :
		print("[-]Problem with finding parameters.")
		print(f"[-]check the url \"{url}\"")
		return 'ERROR'
