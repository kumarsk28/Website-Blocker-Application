# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 18:08:16 2018

@author: Shubham
"""

import time 
from datetime import datetime as dt 
  
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
  
sitenum = int(input("How many sites you want to block/unblock :"))
website_list = []

for i in range(1,sitenum+1):
    website = input("Enter the site url :")
    website_list.append(website)

print("\nFor Unblocking of a website (if present already), the user must enter the start time and end time equal.\n")
start = int(input("Enter the starting time to block the site in 24 hr format : "))
end = int(input("Enter the ending time to block the site in 24 hr format : "))

while True: 
    if dt(dt.now().year, dt.now().month, dt.now().day,start) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,end): 
        
        with open(hosts_path, 'r+') as file: 
            content = file.read() 
            for website in website_list: 
                if website in content: 
                    pass
                else: 
                    file.write(redirect + " " + website + "\n") 
            print("\n Website Blocked Successfully \n")
    else: 
        with open(hosts_path, 'r+') as file: 
            content = file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(website in line for website in website_list): 
                    file.write(line) 
            file.truncate() 
            print("\nFun hours ...Enjoy\n")
    time.sleep(600)
        
