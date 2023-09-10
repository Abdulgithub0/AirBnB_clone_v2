#!/usr/bin/python3
"""do full clean up in both local and remote server"""
from fabric.api import *

env.hosts = ["35.153.18.178", "52.201.158.90"]


def do_clean(number=0):
    """Clean up older versions of archives."""
    number = int(number)
    number = 1 if number == 0 else number
    r_path = "/data/web_static/releases/"
    numb = "+" + str(number + 1)

    # Local cleanup
    with lcd("versions"):
        l_res = local("ls -t | tail -n {}".format(numb))
        if l_res.succeeded:
            l_list = l_res.split()
            for archive in l_list:
                if archive.endswith(".tgz"):
                    local("rm {}".format(archive))

    # Remote cleanup
    with cd(r_path):
        r_res = run("ls -t | tail -n {}".format(numb))
        if r_res.succeeded:
            r_list = r_res.split()
            for archive in r_list:
                if "web_static_" in archive:
                    sudo("rm -rf {}".format(archive))
            print(r_res.split())
