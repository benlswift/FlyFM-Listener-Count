from urllib.request import urlopen
from xml.dom import minidom
import time

while(1):
    html = urlopen("http://fresh.flyfm.co.uk/flyfm.xspf")
    p = html.read()
    h = p.decode("utf-8")
    res = h.find("Current Listeners:") + 19
    print ("Current Listeners: ", h[res],h[res+1])
    time.sleep(10)
