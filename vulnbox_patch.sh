set -e

sshpass -V > /dev/null

mkdir -p services
sshpass -p ggm6vjma8poowlbxig0iwt0kqfayih0i \
  rsync -r --exclude 'ctffarm' \
  --exclude 'packmate' \
  --exclude 'snap' \
  --exclude '.*' \
  ./services/* root@vulnbox:/root

ssh
