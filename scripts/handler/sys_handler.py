import commands
import sys
sys.path.append('../')
from common.util import log

forbidden_list = ['shutdown', 'halt', 'rm', 'stop']
def syscmdhandler(obj, action, args_list):
    #log('something here')
    if action in forbidden_list:
        return 'forbidden exec command: ' + action
    if action == 'deploy':
        return 'This feature in coding now.'

    else:
        cmd = action if not args_list else action + ' ' + ' '.join(args_list)
        status, out = commands.getstatusoutput(cmd)
        return out if status == 0 else 'cmd error'
