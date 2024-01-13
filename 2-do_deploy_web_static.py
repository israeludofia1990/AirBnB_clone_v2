#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""
from fabric.api import run, put, env
from os.path import exists


env.hosts = ['100.24.253.52', '52.86.163.192']


def do_deploy(archive_path):
    '''distributes an archive to my web servers'''
    if exists(archive_path):
        file_name = archive_path.split('/')[-1]
        file_name_no_ext = file_name.split('.')[0]
        path = "/data/web_static/releases/"
        try:
            put(archive_path, '/tmp/')
            run('mkdir -p {}{}/'.format(path, file_name_no_ext))
            run('tar -xzf /tmp/{} -C {}{}/'.format(file_name,  path,
                file_name_no_ext))
            run('rm /tmp/{}'.format(file_name))
            run('mv {0}{1}/web_static/* {0}{1}/'.format(path,
                file_name_no_ext))
            run('rm -rf {}{}/web_static'.format(path, file_name_no_ext))
            run('rm -rf /data/web_static/current')
            run('ln -s {}{}/ /data/web_static/current'.format(path,
                file_name_no_ext))
            return True
        except Exception as e:
            return False
    return False
