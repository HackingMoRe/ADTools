#!/usr/bin/env python3

import json
import os
import sys

ENV_FILE_PATH = '.env.json'

if os.path.isfile(ENV_FILE_PATH):
    print(f'WARN: {ENV_FILE_PATH} already exists. Nothing done.', file=sys.stderr)
    exit(1)

vulnbox_ip = input('Enter the vulnbox IP: ')
gameserver_url = input('Enter gameserver URL for flag submission: ')
team_token = input('Enter the team token: ')
number_of_teams = int(input('Enter the number of teams: '))
team_ip_format = input('Enter the Python format string for team IP: ')
game_interface = input('Enter network interface name for the game: ')

env = {
    'vulnbox_ip': vulnbox_ip,
    'gameserver_url': gameserver_url,
    'team_token': team_token,
    'number_of_teams': number_of_teams,
    'teams_format': team_ip_format,
    'game_interface': game_interface,
    'root_password': os.urandom(32).hex(),
    'packmate_password': os.urandom(32).hex(),
    'ctffarm_password': os.urandom(32).hex()
}

with open(ENV_FILE_PATH, 'w') as f:
    json.dump(env, f, indent=4)

os.chmod(ENV_FILE_PATH, 0o600)
