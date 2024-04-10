sudo apt-get install git -Y
sudo apt-get update
sudo apt-get install python3 python3-dev python3-pip -Y

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools

git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
