#!/data/data/com.termux/files/usr/bin/bash
clear
echo -e "\033[1;36m[+] UPGRADING SYSTEM...\033[0m"
pkg update -y && pkg upgrade -y
pkg install tor python -y
pip install stem
# Tor Config Fix
rm $PREFIX/etc/tor/torrc
echo "ControlPort 9051" >> $PREFIX/etc/tor/torrc
echo "CookieAuthentication 0" >> $PREFIX/etc/tor/torrc
echo -e "\033[1;32m[!] SETUP FINISHED. RUN python greyip.py\033[0m"