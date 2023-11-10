#!/bin/bash
set -xe
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install libpcsclite-dev pcscd pcsc-tools -y

# sudo systemctl status pcscd.service pcscd.socket
# enable access udev from non-root
sudo sh -c 'echo SUBSYSTEM==\"usb\", ACTION==\"add\", ATTRS{idVendor}==\"054c\", ATTRS{idProduct}==\"06c3\", GROUP=\"plugdev\" >> /etc/udev/rules.d/90-nfc.rules'
# sudo sh -c 'echo blacklist port100 >> /etc/modprobe.d/blacklist-nfc.conf'
sudo udevadm control -R # then re-attach device
