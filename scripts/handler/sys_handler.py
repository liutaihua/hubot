import commands

forbidden_list = ['shutdown', 'halt', 'rm', 'stop']
def syscmdhandler(obj, cmd):
    for i in forbidden_list:
        if i in cmd:
            return 'forbidden exec command: ' + cmd
    status, out = commands.getstatusoutput(cmd)
    return out if status == 0 else 'cmd error'
