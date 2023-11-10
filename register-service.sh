#!/bin/bash
set -xe
sudo cp nyutaisitu.service /etc/systemd/system/
sudo systemctl enable nyutaisitu.service
sudo systemctl start nyutaisitu.service
sudo systemctl status nyutaisitu.service
