#!/usr/bin/env bash

python3 -m venv venv
source ./venv/bin/activate
pip3 install --upgrade pip
python3 main.py
wait $!
