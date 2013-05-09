#coding=utf8

import commands
import sys
sys.path.append('../')
from common.util import log
from common.util import announce

#from fabfile.deploy import deploy
#from fabfile.deploy import deploy_by_rsync

forbidden_list = ['shutdown', 'halt', 'rm', 'stop', 'passwd', 'iptables']
def syscmdhandler(obj, action, args_list):
    #log('something here')
    if action in forbidden_list:
        return 'forbidden exec command: ' + action
    if action == 'deploy':
        return 'This feature in coding now.'

    elif action in ['sync', 'rsync']:
        try:
            ip = args_list[0]
            name = args_list[1]
            announce('Starting update %s: %s NOW...'%(ip, name))
#            deploy_by_rsync(ip, name)
#        except Exception, e:
#            print 22222222, e
#            log(e)
#            return e
#        return '已完成'
            if name == 'flash':
                status, out = commands.getstatusoutput('rsync -az /terminus/hades/static/game/ %s:/terminus/hades/static/game/'%ip)
                file_list = commands.getoutput('ssh root@%s "find /terminus/hades/static/game/ -name game_config.xml"'%ip).split()
                for file in file_list:
                    cmd = 'sed -i "s/<web>http:\/\/.*\/<\/web>/<web>http:\/\/%s\/<\/web>/" %s'%(ip, file)
                    status, out = commands.getstatusoutput("ssh %s '%s'"%(ip, cmd))
            else:
                status, out = commands.getstatusoutput('ssh %s "cd /terminus/%s; git reset --hard; git pull"'%(ip, name))
        except Exception, e:
            log(e + '\n' + status)
            return e + '\n' + status
        return out + '\n已完成' if status == 0 else 'cmd error'
        
    else:
        cmd = action if not args_list else action + ' ' + ' '.join(args_list)
        status, out = commands.getstatusoutput(cmd)
        return out if status == 0 else 'cmd error'
