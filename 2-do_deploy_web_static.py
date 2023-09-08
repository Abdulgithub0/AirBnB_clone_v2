#!/usr/bin/env python3
"""
A Fabric script (based on the file 2-do_deploy_web_static.py)
that distributes an archive to your web servers
"""
from fabric.api import *
env.hosts = ["35.153.18.178", "52.201.158.90"]


def do_deploy(archive_path):
    """Deploy web_static files"""
    try:
        if archive_path:
            # Extract the filename from the path
            file_name = archive_path.split("/")[-1]
            sudo("mkdir -p /tmp/")
            put(archive_path, "/tmp/")
            releases = "/data/web_static/releases/" + file_name[:-4]
            sudo("mkdir -p {}".format(releases))
            sudo("tar -xzvf /tmp/{} -C {}/".format(file_name, releases))
            sudo("rm /tmp/{}".format(file_name))
            # relocate files location to allow easy aliasing by nginx
            sudo("mv {}/web_static/* {}".format(releases, releases))
            sudo("rm -rf {}/web_static".format(releases))
            # Check if the symbolic link exists before removing it
            sudo("rm -rf /data/web_static/current")
            sudo("mkdir -p /data/web_static && touch /data/web_static/current")
            # Create a new symbolic link
            sudo("ln -sf {}/ /data/web_static/current".format(releases))
            print("...All the Files have been deployed successfully...")
            return True
    except Exception as e:
        return False
