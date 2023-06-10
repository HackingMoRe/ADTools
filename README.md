# AD Tools
This repo contains all the tools and scripts needed to run and manage 
an Attack and Defence vulnbox.

It contains several tools, some helpers and some tools that were developed
by havce members, tailored to the CyberChallenge.IT 2022 A/D CTF.

Many design decisions are made assuming the CCIT network topology,
so these scripts may not work well for every Attack/Defence CTF.

## Requirements
 - [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
 - Linux host (it can probably be launched also from Windows,
   but I didn't check)
 - `sshpass`

## Deploy
 - `./hosts.sh <vulnbox-ip> <nop-ip>`
 - `ssh root@vulnbox`, type yes to the SSH Auth fingerprint.
    This is needed to add the server SSH fingerprint to `.ssh/known_hosts`
    (Ansible can't do that).
 - While inside of the vulnbox, take note of the interface that runs
   WireGuard.
 - **IMPORTANT:** edit `vulnbox_deploy.yml` to update the relevant variables.
 - On your local machine, type `ansible-playbook vulnbox_deploy.yml -i "vulnbox," -u root --extra-vars "ansible_user=root ansible_password=<your_vulnbox_password>"`, 
   note that the comma after `vulnbox,` is not a typo and it is needed.
 - You can now `ssh@vulnbox` with the new SSH password.
 - On the vulnbox, launch `firewall.sh <port-service-1> <port-service-2> <port-service-3> <port-service4>`. When ready type `Y`.
 - You now have *S4D-Farm* running on port 42069, *packmate* on port 31337
   and a cronjob that every minute checks if any container was shut down.
 - ...
 - pwn all the things!
