#!/usr/bin/python3
""" data pack"""

from fabric.api import *
import time


def do_pack():
    """ create .tgz """

    local("mkdir -p versions")
    created = (time.strftime("%Y%m%d%H%M%S"))
    tgzfile = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(created))
    if not tgzfile.succeeded:
        return None
    else:
        return "versions/web_static_{}.tgz".format(created)
