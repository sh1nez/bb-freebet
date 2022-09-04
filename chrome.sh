#!/usr/bin/env bash

rm -r ~/.cache/selenium
rm -r log.txt

source venv/bin/activate
python3 chrome.py
