#!/bin/bash

# check if python is installed or not

# check if venv exists or not

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
python3 main.py