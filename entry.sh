#!/bin/bash
chmod +x /test/exporter.sh
chmod +x /test/custom_exporter.py
if [ ! -d "/root/.ipfs-cluster/service.json" ]; then
  ipfs-cluster-service init
fi
nohup python3 /test/custom_exporter.py > output1.log 2>&1 &
ipfs-cluster-service daemon
