import os
import time
import sys
import subprocess
import json
import requests
import random
from datetime import datetime
from stem import Signal
from stem.control import Controller
from colorama import init, Fore, Style

# Initialize colorama for cross-platform support
init(autoreset=True)

# Custom Color Schemes (Premium Look)
class Colors:
    PRIMARY = '\033[38;2;100;200;255m'      # Neon Blue
    SECONDARY = '\033[38;2;255;100;100m'    # Neon Red
    ACCENT = '\033[38;2;255;215;0m'         # Gold
    SUCCESS = '\033[38;2;0;255;127m'        # Spring Green
    INFO = '\033[38;2;175;238;238m'         # Turquoise
    DARK = '\033[38;2;30;30;40m'            # Dark Grey
    WHITE = '\033[1;97m'
    RESET = '\033[0m'
    
    # Gradient effects
    @staticmethod
    def gradient(text, start_color, end_color):
        return text  # Simplified for compatibility

# Professional ASCII Banner
def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    banner_art = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════╗
{Colors.PRIMARY}║{Colors.ACCENT}                                                                              {Colors.PRIMARY}║
{Colors.PRIMARY}║{Colors.WHITE}     ███╗   ███╗██╗███╗   ██╗██╗  ██╗ █████╗ ███████╗{Colors.PRIMARY}           ║
{Colors.PRIMARY}║{Colors.WHITE}     ████╗ ████║██║████╗  ██║██║  ██║██╔══██╗╚══███╔╝{Colors.PRIMARY}           ║
{Colors.PRIMARY}║{Colors.WHITE}     ██╔████╔██║██║██╔██╗ ██║███████║███████║  ███╔╝ {Colors.PRIMARY}           ║
{Colors.PRIMARY}║{Colors.WHITE}     ██║╚██╔╝██║██║██║╚██╗██║██╔══██║██╔══██║ ███╔╝  {Colors.PRIMARY}           ║
{Colors.PRIMARY}║{Colors.WHITE}     ██║ ╚═╝ ██║██║██║ ╚████║██║  ██║██║  ██║███████╗{Colors.PRIMARY}           ║
{Colors.PRIMARY}║{Colors.WHITE}     ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝{Colors.PRIMARY}           ║
{Colors.PRIMARY}║{Colors.ACCENT}                                                                              {Colors.PRIMARY}║
{Colors.PRIMARY}╠══════════════════════════════════════════════════════════════════╣
{Colors.PRIMARY}║{Colors.INFO}                      ADVANCED TOR CONTROLLER                         {Colors.PRIMARY}║
{Colors.PRIMARY}║{Colors.SUCCESS}                  CREATOR: MINHAZ | VERSION: 3.0                    {Colors.PRIMARY}║
{Colors.PRIMARY}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}
    """
    print(banner_art)
    print(f"{Colors.ACCENT}├{Colors.WHITE} PROFESSIONAL EDITION{Colors.ACCENT} ───────────────────────────────────────────┤{Colors.RESET}")

def get_current_ip():
    """Fetch current IP with proxy"""
    try:
        proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        response = requests.get('https://api.ipify.org?format=json', proxies=proxies, timeout=10)
        return response.json()['ip']
    except:
        return None

def get_ip_details(ip):
    """Advanced IP Geolocation"""
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}?fields=66846719', timeout=5)
        data = response.json()
        if data['status'] == 'success':
            return data
        return None
    except:
        return None

def display_ip_info(ip):
    """Professional IP Information Display"""
    if ip:
        print(f"{Colors.INFO}├{Colors.WHITE} CURRENT IP{Colors.INFO} ─────────────────────────────────────────────┤{Colors.RESET}")
        print(f"{Colors.SUCCESS}✓{Colors.WHITE} IPv4 Address: {Colors.ACCENT}{ip}{Colors.RESET}")
        
        details = get_ip_details(ip)
        if details:
            print(f"{Colors.SUCCESS}✓{Colors.WHITE} Location: {Colors.PRIMARY}{details.get('city', 'N/A')}, {details.get('country', 'N/A')}{Colors.RESET}")
            print(f"{Colors.SUCCESS}✓{Colors.WHITE} ISP: {Colors.PRIMARY}{details.get('isp', 'N/A')}{Colors.RESET}")
            print(f"{Colors.SUCCESS}✓{Colors.WHITE} Organization: {Colors.PRIMARY}{details.get('org', 'N/A')}{Colors.RESET}")
            print(f"{Colors.SUCCESS}✓{Colors.WHITE} Latitude/Longitude: {Colors.PRIMARY}{details.get('lat', 'N/A')}, {details.get('lon', 'N/A')}{Colors.RESET}")
    else:
        print(f"{Colors.SECONDARY}✗{Colors.WHITE} Failed to fetch IP information{Colors.RESET}")

def start_tor_service():
    """Enhanced Tor Service Management"""
    os.system("pkill -9 tor > /dev/null 2>&1")
    time.sleep(1)
    
    print(f"{Colors.ACCENT}⟳{Colors.WHITE} Initializing Tor Service...{Colors.RESET}")
    
    # Create torrc for better performance
    torrc_content = """
SocksPort 9050
ControlPort 9051
CookieAuthentication 0
HashedControlPassword 
NewCircuitPeriod 30
MaxCircuitDirtiness 60
NumEntryGuards 3
"""
    with open('/tmp/torrc_custom', 'w') as f:
        f.write(torrc_content)
    
    process = subprocess.Popen(['tor', '-f', '/tmp/torrc_custom'], 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
    
    # Wait with animation
    for i in range(5):
        sys.stdout.write(f"\r{Colors.INFO}◉{Colors.WHITE} Establishing Secure Circuit {Colors.PRIMARY}{'█' * i}{'░' * (4-i)}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
    print()
    time.sleep(2)
    return process

class TorController:
    def __init__(self):
        self.rotation_count = 0
        self.start_time = datetime.now()
        self.session_id = random.randint(1000, 9999)
        
    def rotate_ip(self):
        """Advanced IP rotation with authentication"""
        try:
            with Controller.from_port(port=9051) as controller:
                controller.authenticate()
                controller.signal(Signal.NEWNYM)
                time.sleep(1)
                return True
        except Exception as e:
            return False
    
    def display_stats(self):
        """Professional statistics display"""
        uptime = datetime.now() - self.start_time
        print(f"\n{Colors.INFO}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Colors.INFO}║{Colors.ACCENT}                      SESSION STATISTICS                         {Colors.INFO}║")
        print(f"{Colors.INFO}╠══════════════════════════════════════════════════════════════════╣")
        print(f"{Colors.INFO}║{Colors.WHITE} Session ID: {Colors.PRIMARY}{self.session_id}                                                      {Colors.INFO}║")
        print(f"{Colors.INFO}║{Colors.WHITE} Uptime: {Colors.PRIMARY}{str(uptime).split('.')[0]}                                                           {Colors.INFO}║")
        print(f"{Colors.INFO}║{Colors.WHITE} Rotations: {Colors.PRIMARY}{self.rotation_count}                                                           {Colors.INFO}║")
        print(f"{Colors.INFO}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}")

def main():
    banner()
    
    # Initialize controller
    controller = TorController()
    
    # Start Tor service
    start_tor_service()
    
    print(f"{Colors.SUCCESS}✓{Colors.WHITE} Tor Service {Colors.SUCCESS}ACTIVE{Colors.RESET}")
    print(f"{Colors.INFO}◉{Colors.WHITE} Control Port: {Colors.PRIMARY}9051{Colors.RESET}")
    print(f"{Colors.INFO}◉{Colors.WHITE} SOCKS5 Proxy: {Colors.PRIMARY}127.0.0.1:9050{Colors.RESET}")
    print(f"{Colors.ACCENT}├{Colors.WHITE} IP ROTATION MODE{Colors.ACCENT} ─────────────────────────────────────────┤{Colors.RESET}\n")
    
    try:
        while True:
            # Rotate IP with professional feedback
            print(f"{Colors.ACCENT}⟳{Colors.WHITE} Requesting New Identity...{Colors.RESET}")
            
            if controller.rotate_ip():
                controller.rotation_count += 1
                time.sleep(1)  # Wait for Tor to establish new circuit
                
                current_ip = get_current_ip()
                
                if current_ip:
                    print(f"{Colors.SUCCESS}✓{Colors.WHITE} IP Rotation {Colors.SUCCESS}SUCCESSFUL{Colors.RESET}")
                    display_ip_info(current_ip)
                else:
                    print(f"{Colors.SECONDARY}⚠{Colors.WHITE} IP Changed but unable to verify{Colors.RESET}")
            else:
                print(f"{Colors.SECONDARY}✗{Colors.WHITE} Rotation Failed - Restarting Tor...{Colors.RESET}")
                start_tor_service()
                time.sleep(3)
                continue
            
            # Display statistics
            controller.display_stats()
            
            # Professional countdown with gradient
            print(f"\n{Colors.INFO}├{Colors.WHITE} NEXT ROTATION IN{Colors.INFO} ─────────────────────────────────────┤{Colors.RESET}")
            for i in range(10, 0, -1):
                # Color changes based on remaining time
                if i > 7:
                    color = Colors.SUCCESS
                elif i > 4:
                    color = Colors.ACCENT
                else:
                    color = Colors.SECONDARY
                
                sys.stdout.write(f"\r{color}◉{Colors.WHITE} {str(i).zfill(2)} seconds remaining {color}{'⬤' * (11-i)}{Colors.RESET}")
                sys.stdout.flush()
                time.sleep(1)
            
            print("\n" + "─" * 70)
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.SECONDARY}◉◉◉ SHUTTING DOWN ◉◉◉{Colors.RESET}")
        print(f"{Colors.WHITE}Terminating Tor Services...{Colors.RESET}")
        os.system("pkill -9 tor > /dev/null 2>&1")
        
        # Final statistics
        controller.display_stats()
        print(f"\n{Colors.SUCCESS}✓{Colors.WHITE} Service Terminated Successfully{Colors.RESET}")
        print(f"{Colors.ACCENT}Thank you for using MINHAZ TOR Controller{Colors.RESET}\n")
        sys.exit()

if __name__ == "__main__":
    # Check root privileges
    if os.geteuid() != 0:
        print(f"{Colors.SECONDARY}⚠ Warning: Root privileges recommended for best performance{Colors.RESET}")
        time.sleep(2)
    
    # Install required packages if missing
    try:
        import colorama
        import requests
    except ImportError:
        print(f"{Colors.ACCENT}Installing required packages...{Colors.RESET}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama", "requests", "stem"])
    
    main()
