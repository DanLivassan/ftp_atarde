import pysftp


class FtpBeenils():

    def __init__(self, host, username, password):
        self._host = host
        self._username = username
        self._password = password
        self._cnopts = pysftp.CnOpts()
        self._cnopts.hostkeys = None

    def get_articles_xml(self, server_path: str, server_file_name: str):
        with pysftp.Connection(self._host, username=self._username, password=self._password, cnopts=self._cnopts) as sftp:
            if sftp.exists(server_path):
                with sftp.cd(server_path):
                    sftp.get(server_file_name)
            else:
                print("O diretorio {} não existe".format(server_path))

    def set_articles_xml(self, server_path: str, local_file_name: str):
        with pysftp.Connection(self._host, username=self._username, password=self._password, cnopts=self._cnopts) as sftp:
            if sftp.exists(server_path):
                with sftp.cd(server_path):
                    sftp.put(local_file_name)
            else:
                print("O diretorio {} não existe".format(server_path))

    def send_command(self, command):
        with pysftp.Connection(self._host, username=self._username, password=self._password,cnopts=self._cnopts) as sftp:
            r = sftp.execute(command)
            return r


    def chdir(self, path):
        with pysftp.Connection(self._host, username=self._username, password=self._password, cnopts=self._cnopts) as sftp:
            if sftp.exists(path):
                sftp.cd(path)
                print(sftp.execute("ls -l"))
            else:
                print("O diretorio {} não existe".format(path))