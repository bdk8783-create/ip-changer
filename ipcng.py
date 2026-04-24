import os
import time
import sys
import subprocess
from stem import Signal
from stem.control import Controller

# GREY NETHUNTER STYLES
G = '\033[1;90m'  # Grey
W = '\033[1;97m'  # White
C = '\033[1;36m'  # Cyan
R = '\033[1;31m'  # Red
Y = '\033[1;33m'  # Yellow
NC = '\033[0m'    # Reset

def banner():
    os.system('clear')
    print(f"{G}  ________ ___________________{NC}")
    print(f"{G} /  _____/ \______   \_   ___/ {W}IP{NC}")
    print(f"{G}/   \  ___  |       _/|    __)  {NC}")
    print(f"{G}\    \_\  \ |    |   \|     \   {NC}")
    print(f"{G} \______  / |____|_  /\___  /   {NC}")
    print(f"{G}        \/         \/     \/    {NC}")
    print(f"{G}---------------------------------------{NC}")
    print(f"{W} DEVELOPER : {G}GREY NETHUNTER{NC}")
    print(f"{W} FACEBOOK  : {C}fb.com/bangladeshunitedcyber{NC}")
    print(f"{G}---------------------------------------{NC}\n")

def start_tor():
    # Kill existing tor processes to avoid port conflict
    os.system("pkill -9 tor > /dev/null 2>&1")
    print(f"{Y}[*] Starting Tor Service...{NC}")
    subprocess.Popen(['tor'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5) # Wait for Tor to initialize

def change_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            return True
    except:
        return False

banner()
start_tor()

try:
    while True:
        if change_ip():
            print(f"{G}[{W}√{G}] {W}STATUS: {C}IP ROTATED{NC} | {G}GREY-MODE{NC}")
        else:
            print(f"{R}[×] RELOADING TOR SERVICE...{NC}")
            start_tor()
        
        # Countdown effect
        for i in range(5, 0, -1):
            sys.stdout.write(f"\r{W}[•] NEXT CHANGE IN: {Y}{i}s{NC} ")
            sys.stdout.flush()
            time.sleep(1)
        print("\r                                   ", end="\r") 
except KeyboardInterrupt:
    os.system("pkill -9 tor")
    print(f"\n{R}[!] SHUTTING DOWN...{NC}")
    sys.exit()
    