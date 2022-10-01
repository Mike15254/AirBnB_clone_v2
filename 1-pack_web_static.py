#!/usr/bin/python3
"""Compresses static assets"""
from fabric.api import local
from time import strftime


def do_pack():
    """Compresses static assets into a tgz archive"""
    time_of_creation = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(time_of_creation)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except Exception:
        return None
