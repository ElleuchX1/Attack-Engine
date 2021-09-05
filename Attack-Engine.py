#!/usr/bin/python3


#####################
# Stage 2020-2021   #
# SUPCOM            #
#####################

################# ARGUMENT PARSING ####################
import argparse
import requests
import re
import bane
from socket import *
import optparse
from threading import *
parser= argparse.ArgumentParser(description='Attack-Engine Dashbaord')
parser.add_argument('IP',type=str,help="Attacking IP/DNS")
parser.add_argument('PORT',type=int,help="Web server PORT")
args=parser.parse_args()

########################################################

#print(args.IP +' ' +str(args.PORT))


############# VALIDATING IP & DNS  #####################
############# CONVERTING DNS -> IP #####################
from validate_ip import valid_ip
import validators
import socket
x=True
if valid_ip(args.IP):
	pass
elif validators.domain(args.IP):
	x=False
	dns=args.IP
	args.IP=socket.gethostbyname(args.IP)

	#print("VALID DNS")
	#print(args.IP)
else:
	raise Exception('Please Provide A valid IP or DNS name')


if x:
	r = requests.get('http://api.hackertarget.com/reversedns/?q={}'.format(args.IP)).text
	dns = r.split(" ")[1]
	print(dns)

##########################################################



########################### PROMPT #######################

import logo
import os
import ssl
from phonemail import *

from prompt1 import shell


C1=shell(7,'~ ')

#######################INFORMATION GATHERING##############################

def info_gath ():
	prompt="- Available information Gathering Functionalities -"
	print("\33[92m"+prompt)
	print("\t"+"\33[92m"+"[1] Geo IP "+"\33[92m")
	print("\t"+"\33[92m"+"[2] Page Links"+"\33[92m")
	print("\t"+"\33[92m"+"[3] HTTP Headers"+"\33[92m")
	print("\t"+"\33[92m"+"[4] Searching Hosts"+"\33[92m")
	print("\t"+"\33[92m"+"[5] Reverse DNS Lookup"+"\33[92m")
	print("\t"+"\33[92m"+"[6] Shared DNS"+"\33[92m")
	print("\t"+"\33[92m"+"[7] SSL Enumeration"+"\33[92m")
	print("\t"+"\33[92m"+"[8] Email Collector"+"\33[92m")
	print("\t"+"\33[92m"+"[9] Phone Collector"+"\33[92m")
	print("\t"+"\33[92m"+"[10] Links Crawler"+"\33[92m")


	return shell(11," /Information Gathering/ ")

########################################################################


#######################Fuzzing##############################

def fuzzing ():
	prompt="- Available FUZZING Functionalities -"
	print("\33[92m"+prompt)
	print("\t"+"\33[92m"+"[1] Backup Fuzzing "+"\33[92m")
	print("\t"+"\33[92m"+"[2] Directory Fuzzing"+"\33[92m")
	print("\t"+"\33[92m"+"[3] Parameters Fuzzing"+"\33[92m")
	print("\t"+"\33[92m"+"[4] SubDomain Fuzzing"+"\33[92m")



	return shell(5," /Fuzzing/ ")

########################################################################

def misc():
	prompt="- Available  Functionalities -"
	print("\33[92m"+prompt)
	print("\t"+"\33[92m"+"[1] FTP Anonymous Checker "+"\33[92m")
	print("\t"+"\33[92m"+"[2] Port Scanner"+"\33[92m")
	print("\t"+"\33[92m"+"[3] Banner Grabber"+"\33[92m")
	
	return shell(3," /Misc/ ")



from links_crw import *
if C1==1:
	
	C2=info_gath()
	
	while C2 != "EXIT":
	

		if C2==1:
			print('\n')
			r=requests.get('http://api.hackertarget.com/geoip/?q={}'.format(args.IP))
			print('\33[95m'+r.text+'\33[95m')
			print('\n')
		if C2==2:

			r=requests.get('http://api.hackertarget.com/pagelinks/?q={}'.format(args.IP))
			print('\33[95m'+r.text+'\33[95m')
		if C2==3:

			r=requests.get('http://api.hackertarget.com/httpheaders/?q={}'.format(args.IP))
			print('\33[95m'+r.text+'\33[95m')
		if C2==4:

			r=requests.get('http://api.hackertarget.com/hostsearch/?q={}'.format(dns))
			print('\33[95m'+r.text+'\33[95m')
		if C2==5:

			r=requests.get('http://api.hackertarget.com/reversedns/?q={}'.format(args.IP))
			print('\33[95m'+r.text+'\33[95m')
		if C2==6:

			r=requests.get('http://api.hackertarget.com/findshareddns/?q={}'.format(args.IP))
			print('\33[95m'+r.text+'\33[95m')
		if C2==7:
			
			ctx = ssl.create_default_context()
			s = ctx.wrap_socket(socket.socket(), server_hostname=dns)
			
			s.connect((dns, 443))
			cert = s.getpeercert()
			subject = dict(x[0] for x in cert['subject'])
			issued_to = subject['commonName']
			issuer = dict(x[0] for x in cert['issuer'])
			issued_by = issuer['commonName']
			print('\n')
			print('\33[95m''Certificate details:')
			print('Certificate Owner: {}'.format(issued_to))
			print('Certificate Issuer: {}'.format(issued_by))
			print('Issued Date: {}'.format(cert['notBefore']))
			print('Expiring Date: {}'.format(cert['notAfter']))
			print('Serial Number: {}'.format(cert['serialNumber']))
			print('Version: {}'.format(cert['version']))
			print('\n')
		if C2==8:
			emailcol("http://"+dns)

		if C2==9:
			phonenumbercol("http://"+dns)

		if C2==10:
			
			for x in linkcrawl("http://"+dns)[0]:
				print(x)


		C2=info_gath()


if C1 == 2:
	C2=fuzzing()
	while C2!='EXIT':
		dir_char=input('\33[95m'+'-> Custom path to fuzz [Else leave empty]:')
		code_status=input('\33[95m'+'-> Status code filters [Else leave empty]: ')


		if C2==1:
			print('test')
			ext=[".bak",".~",".swp",".tmp"]

			if os.path.isfile('/usr/share/seclists/Discovery/Web-Content/raft-small-files.txt'):
				file1 = open('/usr/share/seclists/Discovery/Web-Content/raft-small-files.txt', 'r')
			else:
				raise("Seclists not found! - apt install seclists ")
			files = file1.readlines()
			for name in files:
				for backup in ext:
					r=requests.get('http://{}/dir/'.format(args.IP))
					if str(r.status_code) not in code_status:
						print( 'File found! : ',name.strip('\n')+backup)
			C2=fuzzing()

		if C2==2:

			if os.path.isfile('/usr/share/seclists/Discovery/Web-Content/raft-small-directories.txt'):
				file1 = open('/usr/share/seclists/Discovery/Web-Content/raft-small-directories.txt', 'r')
			else:
				raise("Seclists not found! - apt install seclists ")
			files = file1.readlines()
			for name in files:
				
				r=requests.get('http://{}/{}/'.format(args.IP,name))
				if str(r.status_code) not in code_status:
					print( 'Directory found! : ',name)
			C2=fuzzing()






		if C2==3:
			from subdns import *
			dnsfuzz(dns)


def try_xss(url,payload):
	bane.xss(url , payload=str(payload) , timeout=2 )

if C1== 3:
	print('\33[7m' + 'Careful!this Functionality will throw malicious payloads at the target')
	print('\33[7m' + 'This may take minutes to test all the vulnerabilities with different payloads and generate the reports')

	if os.path.isfile('xss.txt'):
		XSS = open('xss.txt', 'r')
	else:
		raise("xss.txt not found!")


	a=linkcrawl("http://"+dns)[0]
	
	#for x in u:
#		print("[+]link ",x)
#		for payload in XSS:
#		
#			try_xss(x,payload)
#			print(u)
#			bane.xss('http://'+dns+x , payload=str(payload) , timeout=2 )
			

			
	
	from detectsqli import *
	SQLi(IP)



########### cms detect ################

import cmsdetect

if C1 == 5 :
	cms=cmsdetect.cmsdetector('https://{}/'.format(dns))
	if cms == None : 
		print('[x] CMS Detection failed'  )
	else :
		print('[+] CMS Detected : ',cms)
	C1=shell(11,'~ ')



############## Misc ##################
def login(host):
    try:
        login_ftp=ftplib.FTP(host)
        ftp.login('anonymous','')
        
        ftp.quit()
        return '|+| Logged in as Anonymous'
    except:
        return '|-| Failed to login as Anonymous '



def cScan(host,port):
    try:
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((host,port))
        print('/+/ {}/TCP is OPENED'.format(port))
    except:
        print('/-/ {}/TCP is CLOSED'.format(port))
    finally:
        sock.close()
def PortScanner(host,ports):
    try:
        ipFromDNS=gethostbyname(host)
    except:
        print('Failed to resolve {}'.format(host))
    try:
        NameFromIP= gethostbyaddr(ipFromDNS)
        print('/+/ Results For: {}'.format(NameFromIP[0]))     
    except:
        print('/+/ Results for: {}'.format(ipFromDNS))
    setdefaulttimeout(1)

    for port in ports :
        thr=Thread(target=cScan, args=(host,int(port)))
        thr.start()



def retrieveBanner(host,port):
    try:
        socket.setdefaulttimeout(0)
        sock=socket.socket()
        sock.connect((host,port))
        banner=sock.recv(1024)
        return banner
    except:
        return
def graby():
    host =input("|+| Please ENTER your TARGET IP! : ")
    for port in range(1,500): 
        banner= retrieveBanner(host,port)
    
        if banner:
            print("|+| {}:{} : {}".format(host,port,banner))
        
        else:
            print("Sorry, No banner was detected in {} at port {}".format(host,port))







############## Misc ##################
def login(host):
    try:
        login_ftp=ftplib.FTP(host)
        ftp.login('anonymous','')
        
        ftp.quit()
        return '|+| Logged in as Anonymous'
    except:
        return '|-| Failed to login as Anonymous '



def cScan(host,port):
    try:
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((host,port))
        print('/+/ {}/TCP is OPENED'.format(port))
    except:
        print('/-/ {}/TCP is CLOSED'.format(port))
    finally:
        sock.close()
def PortScanner(host,ports):
    try:
        ipFromDNS=gethostbyname(host)
    except:
        print('Failed to resolve {}'.format(host))
    try:
        NameFromIP= gethostbyaddr(ipFromDNS)
        print('/+/ Results For: {}'.format(NameFromIP[0]))     
    except:
        print('/+/ Results for: {}'.format(ipFromDNS))
    setdefaulttimeout(1)

    for port in ports :
        thr=Thread(target=cScan, args=(host,int(port)))
        thr.start()



def retrieveBanner(host,port):
    try:
        socket.setdefaulttimeout(0)
        sock=socket.socket()
        sock.connect((host,port))
        banner=sock.recv(1024)
        return banner
    except:
        return
def graby():
    host =input("|+| Please ENTER your TARGET IP! : ")
    for port in range(1,500): 
        banner= retrieveBanner(host,port)
    
        if banner:
            print("|+| {}:{} : {}".format(host,port,banner))
        
        else:
            print("Sorry, No banner was detected in {} at port {}".format(host,port))


if C1 == 6 :
	C2=misc()
	if C2==1:
		print(Login(IP))
	if C2 == 2  :
		Ports = [i for i in range(60000)]
		PortScanner(IP,Ports)
	if C2 == 3 :
		graby()







