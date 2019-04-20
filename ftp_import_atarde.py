import datetime
import os
import re
import redis
from ftplib import Error
from ftplib import FTP

from constants import *


class FtpImportAtarde:
    def __init__(self, host, username, password):
        self._host = host
        self._username = username
        self._password = password
        self._articles = []

    def get_articles_xml(self, server):
        with FTP(self._host) as ftp:
            ftp.login(self._username, self._password)

            new_date_file_name = self.add_a_day_on_file(server)

            try:

                if not os.path.exists(SERVERS[server]['LOCAL_PATH']):
                    os.mkdir(SERVERS[server]['LOCAL_PATH'])

                if self.get_attempts(server) is None:
                    self.set_attempts(server, 0)

                if int(self.get_attempts(server)) > SERVERS[server]['MAX_ATTEMPTS']:
                    self.add_a_day_on_file(server)
                    self.set_last_name_retrieved(server, new_date_file_name)
                    self.set_attempts(server, 0)

                self.add_attempts(server)

                with open(SERVERS[server]['LOCAL_PATH'] + new_date_file_name, 'wb') as handle:
                    ftp.retrbinary("RETR {}".format(new_date_file_name), handle.write)

                self.set_last_name_retrieved(server, new_date_file_name)
                self.set_attempts(server, 0)
                print("Arquivo disponível para importação: {}".format(SERVERS[server]['LOCAL_PATH'] + new_date_file_name))
            except Error:
                print(Error.__str__())
                os.remove(SERVERS[server]['LOCAL_PATH'] + new_date_file_name)

                print("O arquivo não foi encontrado no servidor")

    def get_last_news_names(self):
        with FTP(self._host) as ftp:
            ftp.login(self._username, self._password)
            ftp.dir(self.format_gn3_ftp_files)

    def format_gn3_ftp_files(self, line):
        pattern = re.compile('\d{4}-\d{2}-\d{2}-JORNAL.xml')
        file_name = re.sub(' +', ' ', line).split(" ")[-1]
        if file_name.split('.')[-1].upper() == 'xml'.upper() and pattern.match(file_name):
            self._articles.append(file_name)

    def list_articles(self):
        return self._articles

    @staticmethod
    def get_last_name_retrieved(server):
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        return r.get(REDIS_KEYS[server]['IMPORT_VAR'])

    @staticmethod
    def set_last_name_retrieved(server, filename):
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        return str(r.set(REDIS_KEYS[server]['IMPORT_VAR'], filename))

    @staticmethod
    def set_attempts(server: str, number_of_attempts: int):
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        return str(r.set(REDIS_KEYS[server]['COUNTS_VAR'], number_of_attempts))

    @staticmethod
    def get_attempts(server):
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        return r.get(REDIS_KEYS[server]['COUNTS_VAR'])

    @staticmethod
    def add_attempts(server: str):
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        attempts = int(r.get(REDIS_KEYS[server]['COUNTS_VAR']))+1
        return str(r.set(REDIS_KEYS[server]['COUNTS_VAR'], attempts))

    @staticmethod
    def get_date_from_filename(filename: str):
        filename_splitted = filename.decode().split('-')
        year = int(filename_splitted[0])
        month = int(filename_splitted[1])
        day = int(filename_splitted[2])
        return datetime.datetime(year, month, day)

    @staticmethod
    def mount_file_name_from_date(date: datetime.datetime):
        return date.strftime('%Y-%m-%d-JORNAL.xml')

    def add_a_day_on_file(self, server):
        last_file = self.get_last_name_retrieved(server)
        last_date = self.get_date_from_filename(last_file)
        new_date_file_name = self.mount_file_name_from_date(last_date + datetime.timedelta(days=1))
        return new_date_file_name



ftp = FtpImportAtarde(SERVERS['GN3']['HOST'], SERVERS['GN3']['USERNAME'], SERVERS['GN3']['PASSWORD'])
#ftp.set_last_name_retrieved('GN3', '2018-05-23-JORNAL.xml')
ftp.get_articles_xml('GN3')
