set -e

sshpass -V > /dev/null

mkdir -p services
sshpass -p 50052179a37112671e53e9cd4a12c3ec16798d3948720a0c7c2f94124edb975b \
  rsync -r --exclude 'ctffarm' \
  --exclude 'packmate' \
  --exclude 'snap' \
  --exclude '.*' \
  ./services/* root@vulnbox:/root

ssh
