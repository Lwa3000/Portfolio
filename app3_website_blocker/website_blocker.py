'''
Description: This python program blocks websites at certain hour of the day to keep the user from going to social sites and productive.
How to run by superuser: 1. change hosts_temp to hosts_path
						 2. Save file in Application folder
						 3. In terminal: sudo crontab -e
						 4. In this vi file, add: @reboot python3 /Users/xxx/Applications/website_blocker.py
						 5. restart the computer
'''

import time
from datetime import datetime as dt # because the expression will be long

hosts_temp="hosts"
hosts_path='/etc/hosts'
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dud119.mail.live.com","www.dud119.mail.live.com","www.gmail.com","gmail.com","mail.gmail.com"]

#want to check current time to be between 8am and 4pm.
while True:
	if dt(dt.now().year,dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
		print("Working hours")
		with open(hosts_temp,'r+') as file:
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+" "+website+"\n")
	else: 
		with open(hosts_temp,'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
				#This line is the same as:
				#for website in website_list:
				#	if website in line:
					file.write(line)
			file.truncate()
		print("Fun hours")
	time.sleep(5)# 5 seconds


