#!/bin/bash
set -x
echo 'このスクリプトは正直あんまり使えませんので手動でやりましょう'
sudo cp nyutaisitu.service /etc/systemd/system/
sudo systemctl daemon-reload 
sudo systemctl restart nyutaisitu.service
watch -n 1 sudo systemctl status nyutaisitu.service
