#!/usr/bin/env python3

import json
import os
import sys

ENV_FILE_PATH = '.env.json'

if os.path.isfile(ENV_FILE_PATH):
    print(f'WARN: {ENV_FILE_PATH} already exists. Nothing done.', file=sys.stderr)
    exit(1)

env = {
    'root_password': os.urandom(32).hex(),
    'packmate_password': os.urandom(32).hex(),
    'ctffarm_password': os.urandom(32).hex()
}

with open(ENV_FILE_PATH, 'w') as f:
    json.dump(env, f, indent=4)

os.chmod(ENV_FILE_PATH, 0o600)
