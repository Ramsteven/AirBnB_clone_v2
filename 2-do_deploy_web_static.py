#!/usr/bin/python3
"""send archive to our server
		with do_deploy: """

from fabric.api import *
from os import path

env.hosts = ['34.73.211.85', '18.234.133.209']


def do_deploy(archive_path):
    """Deploy servers"""
    if path.exists(archive_path) is False:
        return False

    ufile_ = put(archive_path, '/tmp/')
    if ufile_.failed:
        return False

    complete = archive_path.split("/")[-1]
    file_ = complete.split(".")[0]

    run("sudo mkdir -p /data/web_static/releases/{}/".format(file_))
    run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
        format(file_, fileok))

    run("sudo rm /tmp/{}.tgz".format(file_))

    run("sudo mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/".format(file_, fileok))
    run("sudo rm -rf /data/web_static/releases/{}/web_static".
        format(file_))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".
        format(file_))
    return True
