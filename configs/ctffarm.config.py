import os


CONFIG = {
    'DEBUG': os.getenv('DEBUG') == '1',

    'TEAMS': {
        f'Team #{i}': f'10.60.{i}.1'
        for i in range(0, 40)
    },

    'FLAG_FORMAT': r'[A-Z0-9]{31}=',

    'SYSTEM_PROTOCOL': 'ructf_http',

    'SYSTEM_URL': 'http://10.10.10.10/flags',
    'SYSTEM_TOKEN': '275_17fc104dd58d429ec11b4a5e82041cd2',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    # You can safely edit these, they won't get overwritten by
    # Ansible.
    'SUBMIT_FLAG_LIMIT': 100,
    'SUBMIT_PERIOD': 2,
    'FLAG_LIFETIME': 5 * 60,

    'SERVER_PASSWORD': '0z6uzvjt5zciu3i30ezttie2anpczrjl',

    # For all time-related operations
    # This can be safely edited, it won't get overwritten by Ansible.
    'TIMEZONE': 'Europe/Rome',
}
