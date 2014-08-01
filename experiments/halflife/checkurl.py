# Utilities for checking network status
from urlparse import urlparse
import httplib
import socket

def isResolvable(hostname):
    if hostname is None:
        return False
    try:
        host = socket.gethostbyname(hostname)
        return True
    except socket.gaierror:
        return False

def checkUrl(url):
    if url is None or url == "":
        return "BAD-URL"

    o = urlparse(url)
    
    resolvable = isResolvable(o.hostname)
    if not resolvable:
        return "UNRESOLVABLE"

    try: 
        conn = httplib.HTTPConnection(o.netloc, timeout=10)
        conn.request("GET", o.path )
        res = conn.getresponse()
    except socket.timeout:
        return "TIMEOUT"
    except Exception as e:
        if str(e) == "[Errno 65] No route to host":
            return "NOROUTE"
        else:
            print(e)
            return "CONNECTION-FAILED"
    
    #print(res.status, res.reason)
    if res.status / 100 == 2:
        return "OK"
    elif res.status / 100 == 3:
        state = checkUrl(res.getheader('location'))
        return "REDIRECT+"+state
    elif res.status / 100 == 4:
        return "GONE"
    elif res.status / 100 == 5:
        return "ERROR"
    else:
        return "UNKNOWN"

