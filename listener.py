from pynput import mouse
from logger import logger
from screenshot import catureScreen
from datetime import datetime
from threading import Timer

def on_move(x, y):
    logger.info('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    logger.info('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    if not pressed:
        thread = Timer(1, capture)
        thread.start()
        return False

def capture():
    nowTime = datetime.now().strftime("%m%d%H%M%S")
    catureScreen(nowTime)

def doListen():
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click) as listener:
        listener.join()

    listener = mouse.Listener(
            on_move = on_move,
            on_click = on_click,
            )

    listener.start()