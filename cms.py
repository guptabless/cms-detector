import requests
from bs4 import BeautifulSoup
import bcolors
import sys, argparse

def banner():
    print("""
                ░█████╗░███╗░░░███╗░██████╗░░░░░░██████╗░███████╗████████╗███████╗░█████╗░████████╗░█████╗░██████╗░
                ██╔══██╗████╗░████║██╔════╝░░░░░░██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
                ██║░░╚═╝██╔████╔██║╚█████╗░█████╗██║░░██║█████╗░░░░░██║░░░█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
                ██║░░██╗██║╚██╔╝██║░╚═══██╗╚════╝██║░░██║██╔══╝░░░░░██║░░░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗
                ╚█████╔╝██║░╚═╝░██║██████╔╝░░░░░░██████╔╝███████╗░░░██║░░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
                ░╚════╝░╚═╝░░░░░╚═╝╚═════╝░░░░░░░╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                                                                                                        Code by NG          
          """)
if(len(sys.argv)> 2):
    banner()
    if (sys.argv[1] == '-u'):
        try:
            input_url= sys.argv[2]
            status_code=requests.get(input_url).status_code
            input_code=requests.get(input_url)

            parser = argparse.ArgumentParser()
            parser.add_argument("-u", required=True)
            args = parser.parse_args()

            soup = BeautifulSoup(input_code.text, 'html.parser')
            input_word = False
            input_drupal = False
            try:
                    for link in soup.find_all('link'):
                       input_cms = link.get('href')
                       if (input_cms != None):
                            if 'wp-content' in input_cms:
                               input_word =True
                            elif 'core' in input_cms:
                               input_drupal=True
                    if (input_word == True):
                        print(bcolors.BOLD + 'Application is using Word press')
                    if (input_drupal == True):
                        print(bcolors.BOLD + 'Application is using Drupal')
            except:
                    print(bcolors.OKMSG + "CMS not detected")
        except:
            print(bcolors.ERRMSG + 'Please enter python cms.py -u <valid URL with http:// or https://> ')
    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: cms.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                            'show this help message and exit' '\n''-u URL of any website whoose cms you want to check,   --url URL')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from (-u) or -h, with a valid domain name')


