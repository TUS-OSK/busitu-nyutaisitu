#!/bin/bash
set -xe
#sudo apt-get update
#sudo apt-get upgrade -y
#sudo apt-get install libpcsclite-dev pcscd pcsc-tools -y

sudo systemctl status pcscd.service pcscd.socket
