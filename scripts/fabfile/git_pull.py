from fabric.tasks import Task, execute
from fabric.api import run

def excute_remote_git_pull():
    run('cd /terminus/hades; git reset --hard;git pull')


