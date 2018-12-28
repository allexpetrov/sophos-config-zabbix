#!/bin/python

import sys
import requests
import logging
import urllib3
from requests.auth import HTTPBasicAuth
### mute SSL errors ###

urllib3.disable_warnings()

"""### start logging ###
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True"""

### define static variables

json_start = "{\"data\":[" # first JSON line
json_end = 	"]}" # last JSON line

### to verify the SSL certificate or not to verify the SSL certificate. Accepted: True/False

verification = False

### define passed arguments ###

host = sys.argv[1]
port = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
method = sys.argv[5]
call_type = sys.argv[6]


### Sophos UTM API related parameters ###
sophos_headers = {
	"Accept": "application/json"
}

### testing the API method with automatic discoverty ###

def universal_method(host,port,method,call_type,username,password):
	call=requests.get(
					"https://" + host + ":" + str(port) + "/api/objects/" + str(method) + "/" + str(call_type) + "/",
					headers=sophos_headers,auth=HTTPBasicAuth(username, password), verify=verification)
	json_formatted_output=call.json()
	print json_start
	for num in (range(0, len(json_formatted_output))):
		object_items_count = len(json_formatted_output[num]) - 1
		print "{"
		for key,value in json_formatted_output[num].iteritems():
			if object_items_count >= 1:
				object_items_count -= 1
				print "\"{#" + key.upper() + "}\":\"" + str(value) + "\","
			elif object_items_count == 0:
				print "\"{#" + key.upper() + "}\":\"" + str(value) + "\""
		if num <> len(json_formatted_output) - 1:
			print "},"
		elif num == len(json_formatted_output) - 1:
			print "}"
	print json_end
universal_method(host,port,method,call_type,username,password)
