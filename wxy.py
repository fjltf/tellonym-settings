  
try:
    import requests
    import time
    import uuid
    import json
    import os
    from os import system
    system("title " + "wxy - @r.rxu / tellonym info changer")
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
except Exception as m:
    print("something wrong\n")
    print(m)
    input()
    exit()

print(Fore.BLUE + """
   
░██╗░░░░░░░██╗██╗░░██╗██╗░░░██╗
░██║░░██╗░░██║╚██╗██╔╝╚██╗░██╔╝
░╚██╗████╗██╔╝░╚███╔╝░░╚████╔╝░
░░████╔═████║░░██╔██╗░░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░██╔╝╚██╗░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░
      """, Fore.GREEN + "Credit @r.rxu - wx#0001")
url = "https://api.tellonym.me/tokens/create"

headers = {
	"Host": "api.tellonym.me",
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Connection": "keep-alive",
	"tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
	"User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
	"Accept-Language": "en",
	} 
us = input(Fore.YELLOW + "Username/Email: ") 
ps = input(Fore.YELLOW + "Password: ") 
data = {
	"activeExperimentId": 0,
	"password": ps,
	"country": "US",
	"deviceName": "wx’s iPhone",
	"deviceType": "ios",
	"lang": "en",
	"limit": 16,
	"email": us
}



req = requests.post(url, json=data, headers=headers)



if "WRONG_CREDENTIALS" in req.text:
	print(Fore.RED + "Login Failed, Try Again")



elif "PARAMETER_MISSING" in req.text:
	print(Fore.RED + "Missing Something, Try Again")

elif "accessToken" in req.text:
	print(Fore.GREEN + "Login Success")
	access = json.loads(req.text)["accessToken"]

else:
	print(Fore.RED + "Error !")
	print(req)
	print(req.text)

  
headers = {
	"Host": "api.tellonym.me",
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Connection": "keep-alive",
	"tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
	"User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
	"Authorization": f"Bearer {access}",
	"Accept-Language": "en",
	} 



snapchat = input(Fore.MAGENTA + "SnapChat Username:")
instagram = input(Fore.MAGENTA +"Instagram Username: ")
twitter = input(Fore.MAGENTA +"Twitter Username: ")
name = input(Fore.MAGENTA +"Display Name: ")
bio = input(Fore.MAGENTA +"Bio: ")
username = input(Fore.MAGENTA +"Username: ")


data = {
	"snapchat": snapchat,
	"displayName": name,
	"tintColor": 2,
	"twitter": twitter,
	"aboutMe": bio,
	"limit": 16,
	"username": username,
	"instagram": instagram
}

urll= "https://api.tellonym.me/accounts/settings"
reqf = requests.post(urll, json=data, headers=headers)


if "USERNAME_ALREADY_IN_USE" in reqf.text:
	print(Fore.RED +"Username Taken, Try Again")

elif f'username":"{username}",' in reqf.text:
	print(Fore.GREEN + "Changed Success")

elif "PARAMETER_INVALID" in reqf.text:
	print(Fore.RED + "Invalid Input")
	
else:
	print(Fore.RED + "Error !")
	print(reqf)
	print(reqf.text)

