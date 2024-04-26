# 데비안 계열 리눅스용
sudo apt update
sudo apt install git -Y
sudo apt install python3 python3-dev python3-pip git -Y

# pwntools 설치
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools

# pwndbg 설치
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
