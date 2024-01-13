#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""


from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
from 2-do_deploy_web_static.py import do_deploy
from 1-pack_web_static.py import do_pack


env.hosts = ['100.24.253.52', '52.86.163.192']


def deploy():
    '''creates and distributes an archive to your web servers'''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
