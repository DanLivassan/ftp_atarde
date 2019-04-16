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
    }
}
SERVERS = \
    {
        'GN3': {
            'HOST': 'ftp.atarde.com.br',
            'USERNAME': 'vivainovacao-xml-gn3',
            'PASSWORD': 'oYMHKHyp',
            'LOCAL_PATH': './GN3_XMLS/',
            'MAX_ATTEMPTS': 2
        }
    }
