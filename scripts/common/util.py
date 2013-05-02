import syslog


def log(text):
    syslog.openlog('Hubot', syslog.LOG_PID, syslog.LOG_LOCAL3)
    syslog.syslog(text)
