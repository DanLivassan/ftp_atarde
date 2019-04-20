import datetime
import os
import re
import redis
from ftplib import Error
from ftplib import FTP
import paramiko
from constants import *


class FtpExportAtarde:
    def __init__(self, server: str):
        self._server = server

    def set_file_on_server(self):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(
            SERVERS[self._server]['HOST'],
            SERVERS[self._server]['PORT'],
            username=SERVERS[self._server]['USERNAME'],
            password=SERVERS[self._server]['PASSWORD'],
            timeout=4
        )

        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        sftp = s.open_sftp()
        now = datetime.datetime.now()
        sftp.put(r.get(REDIS_KEYS[self._server]['EXPORT_VAR']), SERVERS[self._server]['EXPORT_EXTERNAL_PATH'] + now.strftime('%Y-%m-%d-%H%M%S-')+self._server+'.xml')


list_of_servers = ['OPERA', 'UOL', 'ELETROMIDIA', 'RSS']
for server in list_of_servers:
    ftp = FtpExportAtarde(server)
    ftp.set_file_on_server()
