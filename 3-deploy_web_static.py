#!/usr/bin/python3
"""
a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to server using the function deploy
"""
from fabric.api import *
from datetime import datetime
env.hosts = ["35.153.18.178", "52.201.158.90"]


def do_pack():
    """archive all files web_static folder"""
    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_{}.tgz".format(time)
    res = local("tar -cvzf {} web_static".format(name))
    if res.failed:
        return None
    return name


def do_deploy(archive_path):
    """Deploy web_static files"""
    try:
        file_name = archive_path.split("/")[-1]
        sudo("mkdir -p /tmp/")
        put(archive_path, "/tmp/")
        releases = "/data/web_static/releases/" + file_name[:-4]
        sudo("mkdir -p {}".format(releases))
        sudo("tar -xzf /tmp/{} -C {}/".format(file_name, releases))
        sudo("rm /tmp/{}".format(file_name))
        # relocate files location to allow easy aliasing by nginx
        sudo("mv {}/web_static/* {}".format(releases, releases))
        sudo("rm -rf {}/web_static".format(releases))
        # Check if the symbolic link exists before removing it
        sudo("rm -rf /data/web_static/current")
        # sudo("mkdir -p /data/web_static && touch /data/web_static/current")
        # Create a new symbolic link
        sudo("ln -sf {}/ /data/web_static/current".format(releases))
        print("...All the Files have been deployed successfully...")
        return True
    except Exception as e:
        return False


def deploy():
    """handle archive of static files and deployment to server"""
    val = do_pack()
    return do_deploy(val) if val else False
