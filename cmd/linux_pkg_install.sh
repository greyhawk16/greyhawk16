# 데비안 계열 리눅스용
sudo apt update
sudo apt install binutils -Y
sudo apt install git python3 python3-dev python3-pip git -Y

# pwntools 설치
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools

# pwndbg 설치
sudo apt install gdb -Y
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh

# docker 설치
sudo apt install docker.io -Y
sudo systemctl start docker
sudo groupadd docker
sudo usermod -aG docker $USER   # docker 그룹에 현재 사용자를 추가 -> sudo 없이 docker 실행가능

# docker-compose 설치
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.26.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose