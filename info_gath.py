from prompt1 import shell
from main import *
import requests
prompt="- Available information Gathering Functionalities -"
print("\33[92m"+prompt)
print("\t"+"\33[92m"+"[1] Geo IP "+"\33[92m")
print("\t"+"\33[92m"+"[2] Page Links"+"\33[92m")
print("\t"+"\33[92m"+"[3] HTTP Headers"+"\33[92m")
print("\t"+"\33[92m"+"[4] Searching Hosts"+"\33[92m")
print("\t"+"\33[92m"+"[5] DNS Lookup"+"\33[92m")
print("\t"+"\33[92m"+"[6] Shared DNS"+"\33[92m")
C2=shell(6," /Information Gathering/ ")



if C2==1:

	r=requests.get('http://api.hackertarget.com/geoip/?q={}'.format(args.IP))
	print(r.text)
	