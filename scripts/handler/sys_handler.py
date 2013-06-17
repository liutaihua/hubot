#coding=utf8

import re
import commands
import sys
sys.path.append('../')
from common.util import log
from common.util import announce

#from fabfile.deploy import deploy
#from fabfile.deploy import deploy_by_rsync


re_ipv4 = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

forbidden_list = ['shutdown', 'halt', 'rm', 'stop', 'passwd', 'iptables']

def syscmdhandler(obj, action, args_list):
    #log('something here')
    if action in forbidden_list:
        return 'forbidden exec command: ' + action
    if action == 'deploy':
        try:
            ip = re_ipv4.findall(' '.join(args_list))
            if not ip:
                return 'please special server IP'
            ip = ip[0]
            name = args_list[0]
            announce('Starting update %s: %s NOW...'%(ip, name))

            if name == 'flash':
                status, out = commands.getstatusoutput('rsync -avz /terminus/hades/static/game/ %s:/terminus/hades/static/game/'%ip)
                file_list = commands.getoutput('ssh root@%s "find /terminus/hades/static/game/ -name game_config.xml"'%ip).split()
                for file in file_list:
                    cmd = 'sed -i "s/<web>http:\/\/.*\/<\/web>/<web>http:\/\/%s\/<\/web>/" %s'%(ip, file)
                    status, _out = commands.getstatusoutput("ssh %s '%s'"%(ip, cmd))
            elif name in ['hades', 'hera', 'zeus', 'poseidon', 'hermes']:
                status, out = commands.getstatusoutput('ssh %s "cd /terminus/%s; git reset --hard; git pull"'%(ip, name))
            else:
                return 'unknown project name'
        except Exception, e:
            log(e + '\n' + status)
            return e + '\n' + status
        if len(out) > 200:
            out = out[200:]
        return out + '\n已完成' if status == 0 else 'cmd error'

    elif action == 'deployself':
        try:
            status, out = commands.getstatusoutput('cd /terminus/hades && git reset --hard && git pull')
            status, out = commands.getstatusoutput('cd /terminus/crown && git reset --hard && git pull')
            out = commands.getoutput('supervisorctl -c /etc/supervisord.conf stop Gameserveradmin && killall ares')
            out = commands.getoutput('rsync -az root@172.26.64.3:/terminus/crown/bin/ /terminus/crown/bin/')
            out = commands.getoutput('cd /terminus/hades/bin/ && python restart restart_gs.py')
        except Exception, e:
            return e + '\n' + status
        return out + '\n已完成' if status == 0 else 'deployself occur error'

    elif action == 'help':
        res = '''
        sys  deploy  [Project Name]  to   [Server IP]        -->  Deploy Project. Example:  sys deploy hades to 172.16.8.106
        sys  [Command Name]                           -->  Execute shell commands
        
        已支持项目:
        sys deploy  [hades | crown | flash | zeus | poseidon | hermes]  to 172.26.64.[3|4]
        sys deployself
        '''
        return res
        
    else:
        cmd = action if not args_list else action + ' ' + ' '.join(args_list)
        status, out = commands.getstatusoutput(cmd)
        return out if status == 0 else 'cmd error'
