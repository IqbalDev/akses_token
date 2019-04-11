# Team: Life Of Programmer
# Mod By: Iqbalz Noobs
# klo gak ada passion jangan jadi programmer, ngoding itu berat kamu gk akan kuat...

import os
import sys
import time
import json
import requests


w = "\033[90;1m" # White dark
r = "\033[91;1m" # red
g = "\033[92;1m" # green
y = "\033[93;1m" # yellow
p = "\033[94;1m" # pink
bl = "\033[96;1m"

pu = "\033[97;1m" # white light


def runntxt(s):
                for c in s + '\n':
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(10. / 100)
def banner_noobs():
                os.system('clear')
                print " "
                os.system('toilet -f small "Iqbalz Tools" -F gay')
                os.system('date | lolcat')
                print " "
                runntxt(bl+"     L I F E   O F   P R O G R A M M E R")
                print pu+"+-------------------------------------------+"
                print "| Mod By: Iqbalz Noobs                       |"
                print "| FB    : Iqbalznoobs                        |"
                print "| Github: https://www.github.com/IqbalzNoobs |"
                print g+ "+-------------------------------------------+"
                print " "
                print "   D A P A T K A N  A C C E S S  T O K E N"
                print "  F A C E B O O K  K A M U  S E K A R A N G"
                print "+-------------------------------------------+"
                 
banner_noobs()

user_noobs = raw_input(r+'[?] \033[96mUsername FB lu Tod\033[97m: ')
passwordlu = raw_input(g+'[?] \033[95mPassword FB lu Tod\033[97m: ')
iqbalz_noobs = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user_noobs+'&locale=en_US&password='+passwordlu+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

lop = iqbalz_noobs.content
bacot = json.loads(lop)
if "session_key" in lop:
                print " "
                runntxt(w+" Loading..........")
		print pu+"[+] Token Fb Anda adalah \033[91m=>\033[92m " + bacot["access_token"]
		open(user_noobs+"iqbalz_token.txt", 'a').write(bacot["access_token"])
		print " "
		print w+"        T O K E N  S U C C E S S "
                print w+"                  T O D"
                print pu+" "
                runntxt(bl+' T H A N K S..  S E M O G A  B E R M A N F A A T... ')
                print pu+" "
else:
		print r+"Login Gagal Cuk...."
		print " "
                print w+" "
