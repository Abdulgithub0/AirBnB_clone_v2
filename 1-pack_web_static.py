#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the
contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """archive all files web_static folder"""
    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_{}.tgz".format(time)
    res = local("tar -cvzf {} web_static".format(name))
    if res.failed:
        return None
    return name
