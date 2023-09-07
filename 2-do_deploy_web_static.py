#!/usr/bin/env python3
"""
a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
"""
from fabric.api import *
env.hosts = ["35.153.18.178", "52.201.158.90"]


def do_deploy(archive_path):
    """deploy web_static files"""
    try:
        if archive_path:
            file_name = archive_path[9:]
            sudo("mkdir -p /tmp/")
            put(archive_path, "/tmp/")
            releases = "/data/web_static/releases/" + file_name[:-4]
            sudo("mkdir -p {}".format(releases))
            sudo("tar -xzvf /tmp/{} -C {}/".format(file_name, releases))
            sudo("rm /tmp/{}".format(file_name))
            if run("test -h /data/web_static/current").succeeded:
                sudo("rm -rf /data/web_static/current")
            sudo("mkdir -p /data/web_static/current")
            sudo("ln -sf {} /data/web_static/current".format(releases))
            return True
    except Exception as e:
        return False
