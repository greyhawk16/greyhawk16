1. EC2 생성(OS: Ubuntu)

2. 필요 패키지 설치
```
sudo apt install gdb -y
sudo apt install gdbserver -y
sudo apt install default-jdk -y
```

3. 로컬에서 Ghidra 압축파일 다운로드 후, 이름을 `Ghidra`로 변경

4. 3의 파일을 EC2로 복사하기
```
scp -i 비밀키이름.pem Ghidra.zip  ubuntu@EC2의_공용_ip_주소:/home/ubuntu/
```

5. 전송받은 `Ghidra.zip` 파일을 EC2에서 압축풀기
```
unzip Ghidra.zip
```

6. `./Ghidra_버전명/server`에서, 아래 명령을 root로 실행
```
./svrInstall
./ghidraSvr start
```
