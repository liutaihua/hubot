#coding=utf8
import subprocess

def deployhandler(obj, action, args_list):
    if action == 'local_sync':
        result = []
        cmd = ['sh', '/terminus/S1/sync_flash_to_ouyang.sh']
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        stdout = p.stdout.readlines()
        result.append(stdout)

        cmd2 = ['sh', '/terminus/S1/gitpull_code.sh']
        p2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE)
        result.append(p2.stdout.readlines())

        return ''.join(result)

