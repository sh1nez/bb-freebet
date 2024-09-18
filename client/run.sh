#!/usr/bin/env bash

if [ -d ~/.cache/selenium ]; then
	rm -r ~/.cache/selenium
fi

venv/bin/python3 chrome.py
