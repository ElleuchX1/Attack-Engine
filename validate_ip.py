import re

def valid_ip(address):

	IPV4 = re.fullmatch('([0-2][0-5]{2}|\d{2}|\d).([0-2][0-5]{2}|\d{2}|\d).([0-2][0-5]{2}|\d{2}|\d).([0-2][0-5]{2}|\d{2}|\d)', address)

	if IPV4:
	    return True

	else:
	    return False

