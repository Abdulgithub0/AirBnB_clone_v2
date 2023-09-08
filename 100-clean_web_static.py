#!/usr/bin/python3
"""
a Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean
"""
from fabric.api import *
env.hosts = ["35.153.18.178", "52.201.158.90"]


def do_clean(number=0):
    """clean up older versions release"""
    number = int(number)
    number = 1 if number == 0 else number
    r_path = "/data/web_static/releases/"
    numb = "+" + str(number + 1)
    with lcd("versions"):
        l_res = local("ls -t | tail -n {}".format(numb))
        r_res = run("ls -t {} | tail -n {}".format(r_path, numb))
        if l_res.succeeded:
            l_list = l_res.stdout.strip().split("\n")
            for archive in l_list:
                if ".tgz" in archive:
                    local("rm {}".format(archive))
    with cd(r_path):
        if r_res.succeeded:
            r_list = r_res.stdout.strip().split("\n")
            for archive in r_list:
                if "web_static_" in archive:
                    sudo("rm -rf {}".format(archive))
