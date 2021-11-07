#!/usr/bin/python3

from rich import print
from rich.console import Console
import os
from validate_ip import valid_ip
import validators
from socket import *
from urllib.parse import urlparse
import requests
import ssl
from phonemail import *
from links_crw import *
import re
import cmsdetect
from threading import Thread
import time
import concurrent.futures
import ftplib
import json



LOGO="""
  ___   _    _                 _             _____                _              
 / _ \\ | |  | |               | |           |  ___|              (_)             
/ /_\\ \\| |_ | |_   __ _   ___ | | __ ______ | |__   _ __    __ _  _  _ __    ___ 
|  _  || __|| __| / _` | / __|| |/ /|______||  __| | '_ \\  / _` || || '_ \\  / _ \\
| | | || |_ | |_ | (_| || (__ |   <         | |___ | | | || (_| || || | | ||  __/
\\_| |_/ \\__| \\__| \\__,_| \\___||_|\\_\\        \\____/ |_| |_| \\__, ||_||_| |_| \\___|
                                                            __/ |                
                                                           |___/                 

- OFFENSIVE SECURITY TOOL # 2020 - 2021
"""



class attack () :
	def __init__(self) :
		self.console = Console()
		error=False
		while True	:		
			try :
				self.target =self.generate_target(error)
				break
			except Exception :
				error = True
		return None

	def logo(self , target=False) :
		os.system("clear")
		self.console.print(LOGO)
		if target :
			print(f"PORT: {self.target['PORT']} \t IP: {self.target['IP']} \t Domain Name: [red]{self.target['domain_name']}[/red] \t URL: {self.target['url']}")
			print("\n")

	def generate_target(self , error=False) :
		self.logo()
		if error : 
			self.console.print('\tTHE URL IS NOT VALID !!! TRY AGAIN .' , style="red blink2")
		self.console.print('Input Target URL ([#8500ff]Exemple : "http://exemple.com"[/#8500ff]) : ' ,end="" , style="red")
		parsed_url = urlparse(input())
		target={}
		target["url"]=parsed_url.scheme+"://"+parsed_url.netloc
		target["domain_name"] = (parsed_url.netloc.split(':'))[0] if ':' in parsed_url.netloc else parsed_url.netloc 
		target["IP"] = target["domain_name"] if valid_ip(target["domain_name"]) else  gethostbyname(target["domain_name"])  
		target["PORT"] = int((parsed_url.netloc.split(':'))[1])  if ':' in parsed_url.netloc else None
		target["PORT"] = {'http' : 80 , 'https' : 443}[parsed_url.scheme] if target["PORT"] == None else target["PORT"]
		return target

	def menu(self , Menu , error=False , dir="") :
		self.logo(True)
		for i in Menu :
			self.console.print("\t"+i)
		if error : 
				self.console.print("\n\tWRONG INPUT !!! TRY AGAIN .", style="red bold blink2")
		self.console.print("~/"+dir+"> " , end='' ,style="#8500ff")
		return input()

	def main (self) :
		error=False
		Menu = ["[1] Information Gathering" , "[2] Fuzzing" ,"[3] Checking for Vulnerabilies" , "[4] Exploiting Vulnerabilies" , "[5] CMS Checking" , "[6] Miscellaneous" , "[7] Explore Findings" ,"[8] Exit " ] 
		while(True) :
			C=self.menu( Menu , error)
			error=False
			if C == '1' :
				self.IG()
			elif C=='2' :
				self.FUZZ()
			elif C=='3' :
				self.CFV()
			elif C=='4' :
				self.EV()
			elif C=='5' :
				self.CMS()
			elif C=='6' :
				self.Misc()
			elif C=='7' :
				self.logo()
				print("\n")
				self.console.print(json.dumps(self.target, skipkeys = True, allow_nan = True, indent = 6))
				self.console.print("Do you want to save as a json file ? [Y/N] :" ,end="", style = "red" )
				if input()[0].upper()=='Y' :
					self.logo()
					self.console.print("Custom Path [Else leave empty]:" , end="" , style="red")
					Input=input()
					f=open(f"{ Input if Input else '.'}/"+self.target["domain_name"]+".json","w")
					f.write(json.dumps(self.target, skipkeys = True, allow_nan = True, indent = 6))
					f.close()
				print('\n')
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='8' :
				exit()
			else :
				error=True
########################     Information Gathering     ##############################
	def  IG(self) :
		Menu = ["[1] Geo IP","[2] Page Links","[3] HTTP Headers","[4] Searching Hosts","[5] Reverse DNS Lookup","[6] Shared DNS","[7] SSL Enumeration","[8] Email Collector","[9] Phone Collector" ,"[10] Links Crawler" ,"[11] Retern"]
		error=False
		while(True) :
			C=self.menu( Menu , error, "Information Gathering")
			error=False
			if C == '1' :
				self.logo(True)
				print('\n')
				with self.console.status("[bold green]Working on it ..." , spinner="dots12") as status:
					r=requests.get('http://api.hackertarget.com/geoip/?q={}'.format(self.target["IP"]))
					self.target["Geo IP"]={x.split(':')[0].strip():x.split(':')[1].strip() for x in r.text.split("\n") }
				self.console.print(r.text)
				print('\n')
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='2' :
				self.logo(True)
				print('\n')
				with self.console.status("[bold green]Working on it ..." , spinner="dots12") as status:
					r=requests.get('http://api.hackertarget.com/pagelinks/?q={}'.format(self.target["IP"]))
				self.console.print(r.text)
				print('\n')
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='3' :
				self.logo(True)
				print('\n')
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:
					r=requests.get('http://api.hackertarget.com/httpheaders/?q={}'.format(self.target["IP"]))
				self.console.print(r.text)
				print('\n')
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='4' :
				self.logo(True)
				print('\n')
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:
					r=requests.get('http://api.hackertarget.com/hostsearch/?q={}'.format(self.target["IP"]))
				self.console.print(r.text)
				print('\n')
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='5' :
				self.logo(True)
				print('\n')
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:
					r=requests.get('http://api.hackertarget.com/reversedns/?q={}'.format(self.target["IP"]))
				self.console.print(r.text)
				print('\n')
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='6' :
				self.logo(True)
				print('\n')
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:
					r=requests.get('http://api.hackertarget.com/findshareddns/?q={}'.format(self.target["IP"]))
				self.console.print(r.text)
				print('\n')
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='7' :
				try :
					self.sslcert()
				except Exception :
					self.console.print('Can\'t find SSL Certificate' , style="red blink2")
					self.console.print('\n')
					self.console.print("Press any key to continue ..." , style = "red" )
					input()
###################

			elif C=='8' :
				self.logo()
				print("\n")
				if "internal_urls" not in self.target :
					self.console.print("The Links Crawler Need To Be Executied Before This Option" , style="red bold")
					print('\n')
					self.console.print("Press any key to continue ..." , style = "red" )
					input()
					self.crw()
				self.logo()
				print("\n")
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:
					with concurrent.futures.ThreadPoolExecutor() as executor:
						emails=executor.map(emailfinder, self.target["internal_urls"])
				self.logo()
				self.target["emails"]=list(set([email for sublist in emails for email in sublist]))
				print(self.target["emails"])
				print('\n')
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='9' :
				self.logo()
				print("\n")
				if "internal_urls" not in self.target :
					self.console.print("The Links Crawler Need To Be Executied Before This Option" , style="red bold")
					print('\n')
					self.console.print("Press any key to continue ..." , style = "red" )
					input()
					self.crw()
				self.logo()
				print("\n")
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:
					with concurrent.futures.ThreadPoolExecutor() as executor:
						Phone_Numbers=executor.map(phonenumberfinder, self.target["internal_urls"])
				self.logo()
				self.target["Phone Numbers"]=list(set([Phone_Number for sublist in Phone_Numbers for email in sublist]))
				print(self.target["Phone Numbers"])
				print('\n')
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='10' :
				self.crw()
			elif C=='11' :
				return
			else :
				error=True
####################################################################################
	
	def crw (self) :
				self.logo(True)
				print('\n')
				self.console.print("Input Max Urls (Default=10) : " , end=""  , style="red" )
				Input=input()
				Max_urls=int(Input)  if re.fullmatch("[0-9]+",Input) else 10
				self.logo(True)
				print('\n')
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:
					links=linkcrawl(self.target['url'],Max_urls)
					self.target["internal_urls"]=list(links[0])
					self.target["external_urls"]=list(links[1])
				self.console.print("Internal Urls :" ,style="red bold")	
				for i in links[0] :
					self.console.print(i,style="blue")	
				self.console.print("External Urls :"  ,style="red bold" )			
				for i in links[1] :	
					self.console.print(i,style="blue")
				print('\n')
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
	

	def sslcert(self) :
		self.logo(True)
		print('\n')
		with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:
			ctx = ssl.create_default_context()
			s = ctx.wrap_socket(socket(), server_hostname=self.target["domain_name"])
			s.connect((self.target["domain_name"], self.target["PORT"]))
			cert = s.getpeercert()
			self.target["SSL Certification"]=cert
			subject = dict(x[0] for x in cert['subject'])
			issued_to = subject['commonName']
			issuer = dict(x[0] for x in cert['issuer'])
			issued_by = issuer['commonName']
		self.console.print('\n')
		self.console.print('[blue]Certificate details:[/blue]')
		self.console.print('[blue]Certificate Owner:[/blue] {}'.format(issued_to))
		self.console.print('[blue]Certificate Issuer:[/blue] {}'.format(issued_by))
		self.console.print('[blue]Issued Date:[/blue] {}'.format(cert['notBefore']))
		self.console.print('[blue]Expiring Date:[/blue] {}'.format(cert['notAfter']))
		self.console.print('[blue]Serial Number:[/blue] {}'.format(cert['serialNumber']))
		self.console.print('[blue]Version:[/blue] {}'.format(cert['version']))
		self.console.print('\n')
		self.console.print("Press any key to continue ..." , style = "red" )
		input()
################################     Fuzzing     ###################################
	def  FUZZ(self) :
		Menu=["[1] Backup Fuzzing","[2] Directory Fuzzing","[3] Parameters Fuzzing","[4] SubDomain Fuzzing" ,"[5] Retern"]
		error=False
		while(True) :
			C=self.menu( Menu , error, "Fuzzing")
			error=False

			if C == '1' :
				self.logo()
				print("\n")
				self.console.print("Custom WordList [Else leave empty]:" , end="" , style="red")
				wordlist=input()
				file1=open(wordlist)
				self.logo()
				self.console.print("Custom Path [Else leave empty]:" , end="" , style="red" )
				path=urljoin(self.target["url"],input())
				path = path if path[-1]!='/' else path[:-1]
				self.logo()
				exts = [".bak",".~",".swp",".tmp"]
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:	
					files = [path+'/'+i if i[0]!="/" else path+i for i in self.add_ext(exts,file1.readlines())]
					with concurrent.futures.ThreadPoolExecutor() as executor:
						found=executor.map(self.fuzzer, files)
				self.logo()
				self.console.print({ i:(j,x) for i,j,x in found	 if i!=None})
				self.console.print("Press any key to continue ..." , style = "red" )
				input()

			elif C=='2' :
				self.logo()
				print("\n")
				self.console.print("Custom WordList [Else leave empty]:" , end="" , style="red")
				wordlist=input()
				file1=open(wordlist)
				self.logo()
				self.console.print("Custom Path [Else leave empty]:" , end="" , style="red" )
				path=urljoin(self.target["url"],input())
				path = path if path[-1]!='/' else path[:-1]
				self.logo()
				self.console.print("Custom Extentions [Else leave empty]:" , end="" , style="red" )
				exts = input().split()
				self.logo()
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:

					files = [path+'/'+i if i[0]!="/" else path+i for i in self.add_ext(exts,file1.readlines())] if exts else [path+'/'+i.strip() if i[0]!="/" else path+i.strip() for i in file1.readlines()]
					with concurrent.futures.ThreadPoolExecutor() as executor:
						found=executor.map(self.fuzzer, files)
					input()
				self.logo()
				self.console.print({ i:(j,x) for i,j,x in found	 if i!=None})
				self.console.print("Press any key to continue ..." , style = "red" )
				input()

			elif C=='3' :
				self.logo()
				print("\n")
				self.console.print("Custom WordList [Else leave empty]:" , end="" , style="red")
				wordlist=input()
				file1=open(wordlist)
				self.logo()
				print("\n")
				self.console.print("# Fixed parameters should be added with the Path if needed ( /exemple?Parameter1=Value1&Paremater2=Value2 )", style="green" )
				self.console.print("Custom Path [Else leave empty]:" , end="" , style="red" )
				path=urljoin(self.target["url"],input())
				path = path if path[-1]!='/' else path[:-1]
				path += '&' if urlparse(path).query else '?'
				self.logo()
				print("\n")
				self.console.print('Custom Value For The Parameter To Fuzz [Else leave empty] :' , end="")
				Value=input()
				Value=Value if Value else '1'
				self.logo()
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:	
					files=[ path+i.strip()+"="+Value for i in file1.readlines() ]
					with concurrent.futures.ThreadPoolExecutor() as executor:
						found=executor.map(self.fuzzer, files)
				self.logo()
				self.console.print({ i:(j,x) for i,j,x in found	 if i!=None})
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='4' :
				self.logo()
				print("\n")
				self.console.print("Custom WordList [Else leave empty]:" , end="" , style="red")
				wordlist=input()
				file1=open(wordlist)
				self.logo()
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:
					files=[ urlparse(self.target["url"]).scheme+"://"+i.strip()+'.'+urlparse(self.target["url"]).netloc for i in file1.readlines() ]
					with concurrent.futures.ThreadPoolExecutor() as executor:
						found=executor.map(self.fuzzer, files)
				input()
				self.logo()
				self.console.print({ i:(j,x) for i,j,x in found	 if i!=None})
				self.console.print("Press any key to continue ..." , style = "red" )
			elif C=='5' :
				return
			else :
				error=True
	def fuzzer(self , file) :
		self.console.print(file)
		r=requests.get(file)
		return (file,r.status_code,len(r.text)) if r.status_code != 404 else (None,None,None)
	def add_ext(self,exts,urls) :
		r=[]
		for i in urls :
			r+=[i.strip()+j for j in exts]
		return r
####################################################################################
	def  CFV(self) :
		pass
	def  EV(self) :
		pass
#################################    CMS Detaction    #############################
	def  CMS(self) : 
		self.logo()
		print("\n")
		cms=cmsdetect.cmsdetector(self.target["url"])
		if cms == None : 
			self.console.print('\t CMS Detection failed'  ,style="#ff0000 bold blink2" )
		else :
			self.console.print('\t CMS Detected : ',cms ,style="#00ff00 bold " )
		self.console.print("Press any key to continue ..." , style = "red" )
		input()
################################     Miscellaneous     ##############################

	def  Misc(self) :
		Menu=["[1] FTP Anonymous Checker" , "[2] Port Scanner" , "[3] Banner Grabber" , "[4] Retern"]
		error=False
		while(True) :
			C=self.menu( Menu , error, "Miscellaneous")
			error=False
			if C == '1' :
				self.logo()
				print("\n")
				with self.console.status("[bold green]Working on it ..." , spinner="dots12" ) as status:
						self.FTPlogin()
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='2' :
				self.logo()
				print("\n")
				self.console.print("Input Ports Range [Default=1000] :" , end="")
				Input=input()
				self.PortScanner([ i for i in range(int(Input) if re.fullmatch("[0-9]+",Input) else 1000) ])	
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='3' :
				self.logo()
				print("\n")
				if "Open Ports" not in self.target :
					self.console.print("The Ports Scanner Need To Be Executied Before This Option" , style="red bold")
					self.console.print("Press any key to continue ..." , style = "red" )
					input()					
					self.logo()
					print("\n")
					self.console.print("Input Ports Range [Default=1000] :" , end="")
					Input=input()
					self.PortScanner([ i for i in range(int(Input) if re.fullmatch("[0-9]+",Input) else 1000) ])	
				self.logo()
				print("\n")
				if self.target["Open Ports"]!=[] :
					self.graby()
				else :
					self.console.print("No Open Ports Found " , style="red blink2")
				self.console.print("Press any key to continue ..." , style = "red" )
				input()
			elif C=='4' :
				return
			else :
				error=True

	def FTPlogin(self):
		try :
			ftp=ftplib.FTP(self.target["IP"])
			ftp.login('anonymous','')  
			ftp.quit()
			self.console.print('|+| Logged in as Anonymous',style="green")
		except:
			self.console.print('|-| Failed to login as Anonymous ' ,style="red")
			


	def PortScanner(self,ports):
			with concurrent.futures.ThreadPoolExecutor() as executor:
				open_ports=[ i for i in executor.map(self.cScan, ports) if i!=None]
			self.logo()
			for i in open_ports :
				self.console.print(f"[green]|+| {i}/TCP is OPENED")
			self.target["Open Ports"]=open_ports

	def retrieveBanner(self,port):
	    try:
	        sock=socket()
	        sock.connect((self.target["IP"],port))
	        banner=sock.recv(1024)
	        return banner
	    except:
	        return

	def graby(self):
	  for port in self.target["Open Ports"] :

	    banner= self.retrieveBanner(port)
	    if banner:
	      self.console.print("|+| {}:{} : {}".format(self.target["IP"],port,banner))
	    else:
	      self.console.print("Sorry, No banner was detected in {} at port {}".format(self.target["IP"],port))

	def cScan(self,port):
			try:
				setdefaulttimeout(0.5)
				sock=socket(AF_INET,SOCK_STREAM)
				sock.connect((self.target['IP'],port))
				print('[green]|+| {}/TCP is OPENED'.format(port) )
				return port
			except:
				print('[red]|+| {}/TCP is CLOSED'.format(port)  )

####################################################################################


def main() :

	Attack=attack()
	Attack.main()
	return
if __name__ == '__main__' :
	main()