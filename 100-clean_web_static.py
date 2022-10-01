#!/usr/bin/python3
"""Compresses and deploys static assets"""
from fabric.api import put, run, env, local, hosts, cd, lcd
from time import strftime
import os


env.hosts = ['3.237.23.148', '3.236.150.39']
archive = None
local_cleaned = False


@hosts('localhost')
def do_pack():
    """Compresses static assets into a tgz archive"""
    time_of_creation = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(time_of_creation)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploys static assets"""
    if not os.path.isfile(archive_path):
        return False

    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(filename, path_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        return True
    except Exception:
        return False


def deploy():
    """Full deployment function"""
    global archive
    if archive is None:
        archive = do_pack()
    if archive is None:
        return False
    success = do_deploy(archive)
    return success


def do_clean(number=0):
    """Deletes out of date versions
<<<<<<< HEAD
=======
>>>>>>> 1dcc7d46e29430daba96ebe9887fe39079e91e36
    Args:
        number: number of most recent files to keep
    """
    global local_cleaned
    number = int(number)
    if number == 0:
        number = 1
    skip = 1 + number
    cmd = 'ls -lt | tail -n+2 | rev | cut -d" " -f1 |\
         rev |  tail -n+{} | xargs -d"\\n" rm -rf'.format(skip)
    if not local_cleaned:
        with lcd("versions"):
            local(cmd)
        local_cleaned = True
    with cd("/data/web_static/releases"):
        run(cmd)
