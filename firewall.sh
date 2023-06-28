#!/bin/bash

if [ $# -lt 4 ]; then
	echo "Usage $0 <port 1> <port-2> <port-3> <port-4>"
	exit 1
fi

ufw default deny incoming
ufw default allow outgoing 
ufw allow 22
docker ps
# service 1
ufw allow $1
# service 2
ufw allow $2
# service 3
ufw allow $3
# service 4
ufw allow $4
# packmate
ufw allow 31337
# tulip
ufw allow 31338
# CTFarm
ufw allow 42069

ufw show added

echo "Enable firewall [Y/n]: "
read x

if [[ $x == 'Y' ]]; then
	ufw enable
else
	exit 1
fi

######################################
# TODO fare in modo di farlo runnare da remoto!