from urllib.request import urlopen
from xml.dom import minidom
from datetime import datetime
import time

initialListeners = 0
midListeners = 0
endListeners = 0
peak = 0
average = 0
while(1):
    
    currentDT = datetime.now()
    hour = currentDT.hour
    minute = currentDT.minute
    html = urlopen("http://fresh.flyfm.co.uk/flyfm.xspf")
    p = html.read()
    h = p.decode("utf-8")
    res = h.find("Current Listeners:") + 19
    listeners = h[res] + h[res+1]
    intList = int(listeners)
    print (hour,":",minute, " ","Current Listeners: ", intList)

    if ( 5 < minute < 15):
        initialListeners = intList
        
    elif ( 29 < minute < 39):
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        midListeners = intList
        
    elif (49 < minute <= 59):
        endListeners = intList
        dayTime =currentDT.strftime("%A %d-%m-%Y %H00")
        average = int(((initialListeners + midListeners + endListeners) /3))
        peak = initialListeners
        if (midListeners > peak):
            peak = midListeners
            if (endListeners > peak):
                peak = endListeners
        elif (endListeners > peak):
            peak = endListeners
        log = dayTime + " Average Listeners: " + str(average) + " Peak Listeners: " + str(peak) + "\n"
        f= open("log.txt","a")
        f.write(log)
        f.close()
        
    time.sleep(600)
