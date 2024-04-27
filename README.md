이 프로그램은 퇴근시간을 설정하면, 이후의 마우스 움직임을 감지하여 로그 파일과 스크린샷 캡처를 남긴다.

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
