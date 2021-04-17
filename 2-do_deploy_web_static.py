#!/usr/bin/python3
""" send  archive to our web servers,
using do_deploy: """

from fabric.api import *
from os import path

env.hosts = ['35.237.158.254', '35.243.174.193']


def do_deploy(archive_path):
    """deploy   servers"""
    if path.exists(archive_path) is False:
        return False

    ufile = put(archive_path, '/tmp/')
    if ufile.failed:
        return False

    complete = archive_path.split("/")[-1]
    s_file = complete.split(".")[0]

    run("sudo mkdir -p /data/web_static/releases/{}/".format(s_file))
    run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
        format(s_file, fileok))

    run("sudo rm /tmp/{}.tgz".format(s_file))

    run("sudo mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/".format(s_file, fileok))
    run("sudo rm -rf /data/web_static/releases/{}/web_static".
        format(s_file))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".
        format(s_file))
    return True
