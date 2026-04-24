pkg update && pkg upgrade -y

pkg install git -y

git clone https://github.com/bdk8783-create/ip-changer

cd ip-changer

chmod +x install.sh

./install.sh

python ipcng.py
