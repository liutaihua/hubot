from fabric.tasks import Task, execute
from fabric.api import run

def remote_git_pull():
    run('cd /terminus/hades; git reset --hard;git pull')

def remote_command(action, host):
    execute(remote_git_pull, hosts=['root@localhost'], roles=[], exclude_hosts=[])
