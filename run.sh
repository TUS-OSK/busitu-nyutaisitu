#!/bin/bash
set -x
export XDG_RUNTIME_DIR=/run/user/1000
echo hello
# /home/pi/busitu-nyutaisitu/venv/bin/python3 -u /home/pi/busitu-nyutaisitu/main.py --device 054c:06c3
/home/pi/busitu-nyutaisitu/venv/bin/python3 -u /home/pi/busitu-nyutaisitu/main.py
