from colorama import init, Fore
import requests # pip install requests
import sys

init()

#colorama Fore
BLUE = Fore.BLUE
GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN

print(f'''
{BLUE} _____ _____ _____ _____ 
{RED}|   | |     |  _  |  _  |
{GREEN}| | | | | | |     |   __|
{CYAN}|_|___|_|_|_|__|__|__|   
                         
''')

nmap = sys.argv[1]

url = 'https://api.hackertarget.com/nmap/?q='
r = requests.get(url+nmap)


print(r.text) # or r.json()