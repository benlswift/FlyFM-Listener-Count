from urllib.request import urlopen
from xml.dom import minidom
from datetime import datetime
import time
import tkinter as tk
window = tk.Tk()
window.title("FLY LISTENERS")
labelfont = ('times', 20, 'bold')
while(1):

    currentDT = datetime.now()
    hour = currentDT.hour
    minute = currentDT.minute
    html = urlopen("http://fresh.flyfm.co.uk/flyfm.xspf")
    p = html.read()
    h = p.decode("utf-8")
    res = h.find("Current Listeners:") + 19
    print (hour,":",minute, " ","Current Listeners: ", h[res],h[res+1])
    label = tk.Label(window, text="Current Listeners: " + h[res],font=("Helvetica", 16)).pack()
    window.update()
    if ( 29 < minute < 39):
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dayTime =currentDT.strftime("%A %d-%m-%Y %H00")
        log = dayTime + " Listeners: " + h[res] + h[res+1]
        f= open("log.txt","a")
        f.write(log)
        f.close()
    #getListeners()
    time.sleep(10)
