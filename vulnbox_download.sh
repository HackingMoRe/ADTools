set -e

sshpass -V > /dev/null

mkdir -p services
sshpass -p ggm6vjma8poowlbxig0iwt0kqfayih0i \
  rsync -r --exclude '/root/ctffarm' \
  --exclude '/root/packmate' \
  --exclude '/root/snap' \
  --exclude '/root/.*' \
  root@vulnbox:/root/* ./services --progress
