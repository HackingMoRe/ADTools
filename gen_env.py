#!/usr/bin/env python3

import json
import os
import sys
import ipaddress

ENV_FILE_PATH = '.env.json'

if os.path.isfile(ENV_FILE_PATH):
    print(f'WARN: {ENV_FILE_PATH} already exists. Nothing done.',
          file=sys.stderr)
    exit(1)


try:
    vulnbox_ip = input('Enter the vulnbox IP: ')
except ValueError:
    print(f'ERROR: {vulnbox_ip} is not a valid IP address')
    exit(1)
gameserver_url = input('Enter gameserver URL for flag submission: ')
if 'http://' not in gameserver_url:
    print(f'ERROR: {gameserver_url} is not a valid url')
    exit(1)
if ':8080' not in gameserver_url:
    print(f'ERROR: {gameserver_url} does not contain a valid port')
    exit(1)
if not gameserver_url.endswith('/flag'):
    print(f'ERROR: {gameserver_url} does not contain a valid endpoint')
    exit(1)
team_token = input('Enter the team token: ')
number_of_teams = int(input('Enter the number of teams: '))
team_ip_format = "f'" + \
    input('Enter the Python format string for team IP: ') + "'"
if '{i}' not in team_ip_format:
    print(f'ERROR: {team_ip_format} is not a valid format string.')
    exit(1)
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

f = open('run_exploit.sh', 'r').readlines()
f[2] = f'\t--server-pass {env['ctffarm_password']} \\\n'
with open('run_exploit.sh', 'w') as file:
    file.writelines(f)
