from __future__ import print_function
import desktopmagic
from desktopmagic.screengrab_win32 \
import(getDisplayRects,saveScreenToBmp,getScreenAsImage,getRectAsImage,getDisplaysAsImages)
import time

def catureScreen(now):
    allMonitors=(getDisplayRects())
    leftMonitor = getRectAsImage(allMonitors[0])
    rightMonitor = getRectAsImage(allMonitors[1])
    leftMonitor.save('./screenshot/{0}_leftMonitor.png'.format(now),format='png')
    rightMonitor.save('./screenshot/{0}_rightMonitor.png'.format(now),format='png')