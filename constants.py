GET = 'get'
PUT = 'put'
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
REDIS_KEYS = {
    'GN3': {
        'IMPORT_VAR': 'GN3_TO_IMPORT',

        'COUNTS_VAR': 'GN3_COUNTS_ATTEMPT'
    },
    'ESTADAO': {
        'IMPORT_VAR': 'ESTADAO_TO_IMPORT',

        'COUNTS_VAR': 'ESTADAO_COUNTS_ATTEMPT'
    },
    'OPERA': {
        'EXPORT_VAR': 'OPERA_TO_EXPORT',
        'COUNTS_VAR': 'OPERA_COUNTS_ATTEMPT'
    },
    'UOL': {
        'EXPORT_VAR': 'UOL_TO_EXPORT',
        'COUNTS_VAR': 'UOL_COUNTS_ATTEMPT'
    },
    'ELETROMIDIA': {
        'EXPORT_VAR': 'ELETROMIDIA_TO_EXPORT',
        'COUNTS_VAR': 'ELETROMIDIA_COUNTS_ATTEMPT'
    },
    'RSS': {
        'EXPORT_VAR': 'RSS_TO_EXPORT',
        'COUNTS_VAR': 'RSS_COUNTS_ATTEMPT'
    }
}
SERVERS = \
    {
        'GN3': {
            'HOST': 'ftp.atarde.com.br',
            'USERNAME': 'vivainovacao-xml-gn3',
            'PASSWORD': 'oYMHKHyp',
            'PORT': 22,
            'LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS/',
            'EXPORT_LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS_EXPORT/',
            'EXPORT_EXTERNAL_PATH': '/home/GN3_EXPORTED/',
            'MAX_ATTEMPTS': 2
        },
        'UOL2': {
            'HOST': 'beenils.com.br',
            'USERNAME': 'root',
            'PASSWORD': 'b7h(VKca',
            'PORT': 22,
            'LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS/',
            'EXPORT_LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS_EXPORT/',
            'EXPORT_EXTERNAL_PATH': '/home/danilo/ftp/files/UOL_EXPORTED/',
            'MAX_ATTEMPTS': 2
        },
        'UOL': {
            'HOST': '157.230.87.132',
            'USERNAME': 'danilo',
            'PASSWORD': '123456ab',
            'PORT': 22,
            'LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS/',
            'EXPORT_LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS_EXPORT/',
            'EXPORT_EXTERNAL_PATH': '/home/danilo/ftp/files/UOL_EXPORTED/',
            'MAX_ATTEMPTS': 2
        },
        'OPERA': {
            'HOST': '157.230.87.132',
            'USERNAME': 'danilo',
            'PASSWORD': '123456ab',
            'PORT': 22,
            'LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS/',
            'EXPORT_LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS_EXPORT/',
            'EXPORT_EXTERNAL_PATH': '/home/danilo/ftp/files/OPERA_EXPORTED/',
            'MAX_ATTEMPTS': 2
        },
        'ELETROMIDIA': {
            'HOST': '157.230.87.132',
            'USERNAME': 'danilo',
            'PASSWORD': '123456ab',
            'PORT': 22,
            'LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS/',
            'EXPORT_LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS_EXPORT/',
            'EXPORT_EXTERNAL_PATH': '/home/danilo/ftp/files/ELETROMIDIA_EXPORTED/',
            'MAX_ATTEMPTS': 2
        },
        'RSS': {
            'HOST': '157.230.87.132',
            'USERNAME': 'danilo',
            'PASSWORD': '123456ab',
            'PORT': 22,
            'LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS/',
            'EXPORT_LOCAL_PATH': '/home/danilo/PythonProjects/sftp/GN3_XMLS_EXPORT/',
            'EXPORT_EXTERNAL_PATH': '/home/danilo/ftp/files/RSS_EXPORTED/',
            'MAX_ATTEMPTS': 2
        },


    }
