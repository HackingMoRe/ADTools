set -e

sshpass -V > /dev/null

mkdir -p services
sshpass -p 50052179a37112671e53e9cd4a12c3ec16798d3948720a0c7c2f94124edb975b \
  rsync -r --exclude '/root/ctffarm' \
  --exclude '/root/packmate' \
  --exclude '/root/snap' \
  --exclude '/root/.*' \
  root@vulnbox:/root/* ./services --progress
