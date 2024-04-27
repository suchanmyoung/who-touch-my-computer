
<img width="732" alt="스크린샷 2024-04-28 오전 3 37 57" src="https://github.com/suchanmyoung/who-touch-my-computer/assets/87016418/bd2262a4-60a1-467a-9531-edf5a6e4d848">

이 프로그램은 퇴근시간을 설정하면 해당 시간 이후 마우스가 움직일 경우 이동경로 로그와 스크린샷을 저장한다.

퇴근시간 이후 켜두고간 컴퓨터를 혹시 누군가 건드리지 않았을까? 

--기분탓일 확률이 높다. 

## Requirements
- pip install pynput
- pip install Pillow --upgrade
- pip install Desktopmagic
- pip install pyautogui
- pip install pypiwin32

## Usage(Background)
- pythonw main.py

## Description
Through this program, you can know who touched my computer after work. also what they did.

1. Log a mouse move or click event in info.log.
2. Capture the screen when you click the mouse
    - For accurate screen recording, Capture works on a new thread 1 second after clicking
3. Use a minimum of 10MB to a maximum of 30MB of memory

## Supported OS
- Windows Only
