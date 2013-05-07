from fabric.tasks import execute
from fabric.api import *
import fabric

@task
def git_pull():
    with fabric.context_managers.settings(hide('warnings', 'running', 'stdout', 'stderr'),warn_only=True):
        with cd('/terminus/hades'):
            run('git reset --hard')
            run('git pull')

@task
def execute_from_local(ip, action):
    if action not in ['hades', 'hera', 'poseidon', 'zeus', 'hermes']:
        path = '/terminus/%s'%action
    elif action == 'flash':
        path = '/terminus/hades/static/game/'
    else:
        return 'error path'
    with fabric.context_managers.settings(hide('warnings', 'running', 'stdout', 'stderr'),warn_only=True):
        local('rsync -az %s %s:%s'%(path, ip, path))

def deploy(host_list):
    execute(git_pull, hosts=host_list)

def deploy_by_rsync(ip, action):
    execute(execute_from_local, ip=ip, action=action, hosts=[], roles=[], exclude_hosts=[])
