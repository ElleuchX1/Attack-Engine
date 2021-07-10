#!/usr/bin/python3

################# ARGUMENT PARSING ####################
import argparse
import requests
import re
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

##########################################################



########################### PROMPT #######################

import logo
import ssl

from prompt1 import shell


C1=shell(6,'~ ')

##########################################################

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


if x:
	r = requests.get('http://api.hackertarget.com/reversedns/?q={}'.format(args.IP)).text
	dns = r.split(" ")[1]
	print(dns)


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
			r=requests.Session()
			s = r.get('http://'+dns)
			print('\n')
			print('\33[95m'+str(re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",s.text)))
			print('\n')
		if C2==9:
			r=requests.Session()
			s = r.get('http://'+dns)
			print('\n')
			print('\33[95m'+str(re.findall("(\(\+?[0-9]+\).[0-9]+.[0-9]+.[0-9]+)",s.text)))
			print('\n')
		if C2==10:
			from links_crw import *
			getlinks('http://'+dns)





		C2=info_gath()
	
	C1=shell(11,'~ ')