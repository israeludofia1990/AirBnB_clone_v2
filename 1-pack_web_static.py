#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    '''generates a .tgz archive from the contents of the web_static folder'''
    date_time = datetime.now()
    f_date_time = date_time.strftime("%Y%m%d%H%M%S")
    try:
        if not isdir("versions"):
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(f_date_time)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        None
