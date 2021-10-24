# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import json
import Hazard
from colorama import Fore

from util.plugins.common import print_slow, setTitle, getheaders

def MassReport(token, guild_id1, channel_id1, message_id1, reason1, Amount):
    Responses = {
            '401: Unauthorized': '[!] Invalid Discord token.',
            'Missing Access': '[!] Missing access to channel or guild.',
            'You need to verify your account in order to perform this action.': '[!] Unverified.'
    }

    payload = {
        'channel_id': channel_id1,
        'message_id': message_id1,
        'guild_id': guild_id1,
        'reason': reason1
    }

    sent = 0
    errors = 0

    for i in range(Amount):
        r = requests.post('https://discord.com/api/v9/report', headers=getheaders(token), json=payload)
        setTitle(f'Sent: {sent} | Errors: {errors}')
        if r.status_code == 201:
            sent += 1
            print(f'{Fore.GREEN}Report Sent {Fore.BLUE}|{Fore.GREEN} ID {message_id1}{Fore.RESET}')
        elif r.status_code in (401, 403):
            errors += 1
            print(Responses[r.json()['message']])
        else:
            errors += 1
            print(f'{Fore.RED} > Error {Fore.BLUE}|{Fore.RED} Status Code: {r.status_code}{Fore.RESET}')
    print_slow(f"\n{Fore.GREEN}Hazardous reporting done! ")
    print("Enter anything to continue. . . ", end="")
    input()
    Hazard.main()