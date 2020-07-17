
import requests
import json
import sys
from os import system

def get_userid(token):
	url = "https://graph.facebook.com/me?access_token=%s" % token
	res = requests.get(url)
	info = json.loads(res.text)
	return info["id"]

def protection(token, enable = True):
	uid = get_userid(token)
	d = 'variables={"0":{"is_shielded": %s,
			"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc",
			"actor_id":"%s",
			"client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(uid))
	h = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % token}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = d, headers = h)
	print("Successfully....")

system("clear")
print("(っ◔◡◔)っ ♥ Facebook Profile protection ♥")
ACCESS_TOKEN = input("ACCESS TOKEN :")
ENABLE = ""
print("")
print("----------------------------------------")
print("")
print("1. Enable protection")
print("2. Disable protection")
input = input("Choose :")
if input == "1": 
    ENABLE = "true"
elif input == "2": 
    ENABLE = "false"
else :
    sys.exit()
protection(ACCESS_TOKEN,ENABLE)
