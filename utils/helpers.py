
import os
import sys
import time
import json
import random
import string
from colorama import init, Fore, Style
from datetime import datetime 

mrh = Fore.LIGHTRED_EX
pth = Fore.LIGHTWHITE_EX
hju = Fore.LIGHTGREEN_EX
kng = Fore.LIGHTYELLOW_EX
bru = Fore.LIGHTBLUE_EX
htm = Fore.LIGHTBLACK_EX
reset = Fore.RESET

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown_timer(seconds):
    while seconds:
        menit, detik = divmod(seconds, 60)
        jam, menit = divmod(menit, 60)
        jam = str(jam).zfill(2)
        menit = str(menit).zfill(2)
        detik = str(detik).zfill(2)
        print(f"{pth}please wait {hju}{jam}:{menit}:{detik}                   ", flush=True, end="\r")
        seconds -= 1
        time.sleep(1)
    print(f"                              ", flush=True, end="\r")
        
def log(message, end="\n", flush=True):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sys.stdout.write(f"{htm}[{current_time}] {message}{end}")
    if flush:
        sys.stdout.flush()   

def _number(number):
    return "{:,.0f}".format(number)

def read_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config.json')
    with open(config_path, 'r') as file:
        try:
            config_content = file.read()
            return json.loads(config_content)
        except json.JSONDecodeError as e:
            return {}

def print_banner():
    banner = r"""{Fore.GREEN}
   ___                   _      __  __      _                 _ 
  / _ \ _ _ _ _ _ _  ___| |__  |  \/  |__ _| |_  _ __ _  _ __| |
 | (_) | '_| '_| ' \/ _ \ '_ \ | |\/| / _` | ' \| '  \ || / _` |
  \___/|_| |_| |_||_\___/_.__/ |_|  |_\__,_|_||_|_|_|_\_,_\__,_|
                                                                
    Auto Claim Bot For Memefi - Orrnob's Drop Automation
    Author  : Orrnob Mahmud
    Github  : https://github.com/OrrnobMahmud
    Telegram: https://t.me/verifiedcryptoairdops
        {Style.RESET_ALL}"""

def generate_random_nonce(length=52):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))