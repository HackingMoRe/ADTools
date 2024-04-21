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
  0. (optional): each team member should generate an SSH key pair and add their public key to the `ssh_keys` file
      ```sh
      # 1. generate a new SSH key pair without passphrase and save it in ~/.ssh/vulnbox_ed25519{,.pub}
      ssh-keygen -t ed25519 -C "your name" -f ~/.ssh/vulnbox_ed25519 -N ""
      # 2. print the public key
      # add the output of this command to the ssh_keys file
      cat ~/.ssh/vulnbox_ed25519.pub
      ```
  1. `sudo ./hosts.sh <vulnbox-ip [<nop-ip>]`: add the IP address of the vulnbox (and, optionally, the IP address of the NOP team) to your `/etc/hosts` file.\
   This is required because Ansible will reference the vulnbox using the hostname `vulnbox`, not the IP address;
  2. connect to the vulnbox and retrieve the name of the network interface that runs WireGuard.\
  Typically, it should be `game` or something similar;
  3. on your local machine, run `./gen_env.py` and provide the required information;
  4. on your local machine, run `ansible-playbook vulnbox_deploy.yml -i "vulnbox," -u root --extra-vars "ansible_user=root ansible_password=<vulnbox password>" --extra-vars "@.env.json"` to deploy all the tools on the vulnbox.\
    Note that the comma after `vulnbox,` is not a typo and it is needed.
  5. connect to the vulnbox using the `root_password` in the `.env.json` file on your local machine;
  6. on the vulnbox, launch `firewall.sh <port-service-1> <port-service-2> <port-service-3> <port-service4>`. When ready type `Y`;
  7. you now have *S4D-Farm* running on port 42069, *packmate* on port 31337 and a cronjob that every minute checks if any container was shut down.
  8. pwn all the things!
