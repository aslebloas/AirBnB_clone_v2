#!/usr/bin/python3
# script that generates a .tgz archive from the contents of
# the web_static folder of your AirBnB Clone repo, using the function do_pack
import os
import tarfile
from datetime import datetime, date, time
from fabric.api import local


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    dpath = "./versions/"
    if not os.path.exists(dpath):
        local("mkdir versions")
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    fpath = dpath + "web_static_" + now + ".tgz"
    local("tar -cvzf {}  web_static".format(fpath))
