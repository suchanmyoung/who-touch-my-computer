from datetime import datetime
from listener import doListen
import time

hoursAndMinutesExpression = "%H%M"
quittingTime = "1735"

while(True):
    now = datetime.now().strftime(hoursAndMinutesExpression)
    if(now > quittingTime):
        doListen()
    time.sleep(0.5)