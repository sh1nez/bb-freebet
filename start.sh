#!/usr/bin/env bash

active_dir="/usr/local/src/bb-freebet"

if [ ! -d "$active_dir"/venv ]; then
	python3 -m venv "$active_dir"/venv
fi

source "$active_dir"/venv/bin/activate
pip3 install -r requirements.txt

cp services/parser.service /etc/systemd/system/
cp services/clean.service /etc/systemd/system/
cp services/clean.timer /etc/systemd/system/

systemctl daemon-reload

systemctl enable --now parser.service
systemctl enable --now clean.timer
