#!/usr/bin/python3
# script that generates a .tgz archive from the contents of
# the web_static folder of your AirBnB Clone repo, using the function do_pack
import os
import tarfile
from datetime import datetime
from fabric.api import local, put, env, run, sudo

env.hosts = ['35.196.156.208', '35.237.160.254']
env.user = 'ubuntu'


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    dpath = "./versions/"
    if not os.path.exists(dpath):
        local("mkdir versions")
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    fpath = dpath + "web_static_" + now + ".tgz"
    local("tar -cvzf {}  web_static".format(fpath))

def do_deploy(archive_path):
    """distributes an archive to your web servers
    Args:
        archive_path: path to archive
    """
    if not os.path.exists(archive_path):
        return False

    # Upload archive to server tmp directory
    put(archive_path, '/tmp/')

    # Uncompress the archive to a folder
    filename = archive_path.split('/')
    length = len(filename)
    filename = filename[length - 1].split('.')[0]

    dest = "/data/web_static/releases/" + filename

    sudo("mkdir -p {}/".format(dest))
    sudo("tar -xzf /tmp/{}.tgz -C {}/".format(filename, dest))
    sudo("rm /tmp/{}.tgz".format(filename))
    sudo("rm -rf /data/web_static/current")
    sudo("ln -s {} /data/web_static/current".format(dest))
