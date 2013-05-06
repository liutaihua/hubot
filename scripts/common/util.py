import syslog
import urllib, urllib2


def log(text):
    syslog.openlog('Hubot', syslog.LOG_PID, syslog.LOG_LOCAL3)
    syslog.syslog(text)


def announce(msg):
    url = "http://localhost:9898/broadcast/create"
    values = {
        'message': msg
    }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    res = urllib2.urlopen(req)
    return res.read()
