# -*- coding: utf-8 -*-
from ftp_beenils import FtpBeenils
import sys, redis
from constants import *
#python main.py beenils.com.br root get /root/ftp 1.41.1.2019.02.20.53.EC.xml
from ftplib import FTP
actions = [GET, PUT]
try:
    server = sys.argv[1]
    action = sys.argv[2]
    path = sys.argv[3]
    file = sys.argv[4]
except IndexError:
    print("O comando deve ser: \n\npython main.py host username password action path file")
    exit(0)
if action not in actions:
    print("As ações do 4º parâmetro tem que ser put ou get!")
    exit(0)
server_s = SERVERS[server]
print(server_s)
exit()
ftp = FtpBeenils(server_s['HOST'], server_s['USERNAME'], server_s['PASSWORD'])

if action == GET:
    ftp.get_articles_xml(path, file)
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    r.set(REDIS_KEYS[server], file)
else:
    ftp.set_articles_xml(path, file)






