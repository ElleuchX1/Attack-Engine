from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style

def shell(n,mypath):
	style = Style.from_dict({
    
    '':          '#ff0066',
    'username': '#884444',
    'at':       '#00aa00',
    'colon':    '#0000aa',
    'pound':    '#00aa00',
    'host':     '#884444',
    'path':     '#ffffff'
    
	})

	message = [
    ('class:username', 'root'),
    ('class:at',       '@'),
    ('class:host',     'Attack-Engine'),
    ('class:colon',    ':'),
    ('class:path',    "{}".format(mypath)),
    ('class:pound',    '#>')
    
	]


	C1 = prompt(message, style=style)
	try:
		C1=int(C1)

	except:

		if C1=="HELP":
			print("\33[34m"+"Choose An Option from 1 to "+str(n))

		else:
			print("\033[91m" + 'Error! The only VALID strings are HELP and EXIT' + "\033[0m")
	
	while (C1 not in range(0,n)) and (C1!="HELP") and (C1!="EXIT") :
		print("\033[91m" + 'Error! Please Provide A valid Number' + "\033[0m")
		C1 = prompt(message, style=style)
		try:
			C1=int(C1)
		except:
			if C1=="HELP":
				print("\33[34m"+"Choose An Option from 1 to "+str(n))
			else:
				print("\033[91m" + 'Error! The only VALID strings are HELP and EXIT ' + "\033[0m")
	
	return C1