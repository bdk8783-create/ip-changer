pkg update && pkg upgrade -y

pkg install git -y

git clone https://github.com/anonym793/GREY-IP.git

cd GREY-IP

chmod +x install.sh

./install.sh

python greyip.py